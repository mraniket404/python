# # Example usage of the functions
# if __name__ == "__main__":
#     # Add notes
#     add_note("Python Tips", "List comprehensions are awesome!", ["python", "tips"])
#     add_note("Shopping", "Buy milk, eggs, and bread", ["personal", "shopping"])
    
#     # Search notes
#     results = search_notes("python")
#     for note in results:
#         display_note(note)
    
#     # Filter by tags
#     personal_notes = filter_by_tags(["personal"])
    
#     # Get statistics
#     stats = get_note_statistics()
#     print(f"Total notes: {stats['total_notes']}")
    
#     # Export notes
#     export_to_text("my_notes.txt")
    
#     # Create backup
#     backup_notes()



import json
import os
from datetime import datetime
from typing import List, Dict, Optional

# File handling functions
def create_note_file(filename: str = "notes.json") -> None:
    """Create a new notes file if it doesn't exist"""
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)

def load_notes(filename: str = "notes.json") -> List[Dict]:
    """Load all notes from file"""
    create_note_file(filename)
    with open(filename, 'r') as f:
        return json.load(f)

def save_notes(notes: List[Dict], filename: str = "notes.json") -> None:
    """Save notes to file"""
    with open(filename, 'w') as f:
        json.dump(notes, f, indent=4)

# CRUD Operations
def add_note(title: str, content: str, tags: List[str] = None, 
             filename: str = "notes.json") -> Dict:
    """Add a new note"""
    notes = load_notes(filename)
    
    note = {
        'id': len(notes) + 1,
        'title': title,
        'content': content,
        'tags': tags or [],
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    notes.append(note)
    save_notes(notes, filename)
    return note

def get_note(note_id: int, filename: str = "notes.json") -> Optional[Dict]:
    """Get a single note by ID"""
    notes = load_notes(filename)
    for note in notes:
        if note['id'] == note_id:
            return note
    return None

def update_note(note_id: int, title: str = None, content: str = None, 
                tags: List[str] = None, filename: str = "notes.json") -> bool:
    """Update an existing note"""
    notes = load_notes(filename)
    
    for note in notes:
        if note['id'] == note_id:
            if title:
                note['title'] = title
            if content:
                note['content'] = content
            if tags is not None:
                note['tags'] = tags
            note['updated_at'] = datetime.now().isoformat()
            save_notes(notes, filename)
            return True
    return False

def delete_note(note_id: int, filename: str = "notes.json") -> bool:
    """Delete a note by ID"""
    notes = load_notes(filename)
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes, filename)
    return True

# Search and Filter Functions
def search_notes(keyword: str, filename: str = "notes.json") -> List[Dict]:
    """Search notes by keyword in title or content"""
    notes = load_notes(filename)
    keyword = keyword.lower()
    
    return [note for note in notes 
            if keyword in note['title'].lower() 
            or keyword in note['content'].lower()]

def filter_by_tags(tags: List[str], filename: str = "notes.json") -> List[Dict]:
    """Filter notes by tags"""
    notes = load_notes(filename)
    tags_set = set(tags)
    
    return [note for note in notes 
            if tags_set.intersection(set(note['tags']))]

def get_notes_by_date(date: str, filename: str = "notes.json") -> List[Dict]:
    """Get notes created on a specific date (YYYY-MM-DD)"""
    notes = load_notes(filename)
    
    return [note for note in notes 
            if note['created_at'].startswith(date)]

def get_recent_notes(days: int = 7, filename: str = "notes.json") -> List[Dict]:
    """Get notes from recent days"""
    notes = load_notes(filename)
    cutoff = datetime.now().timestamp() - (days * 86400)
    
    recent = []
    for note in notes:
        note_date = datetime.fromisoformat(note['created_at']).timestamp()
        if note_date > cutoff:
            recent.append(note)
    
    return sorted(recent, key=lambda x: x['created_at'], reverse=True)

# Display and Utility Functions
def display_note(note: Dict) -> None:
    """Display a single note in a formatted way"""
    print(f"\n{'='*50}")
    print(f"ID: {note['id']}")
    print(f"Title: {note['title']}")
    print(f"Tags: {', '.join(note['tags'])}")
    print(f"Created: {note['created_at']}")
    print(f"Updated: {note['updated_at']}")
    print(f"\nContent:\n{note['content']}")
    print(f"{'='*50}\n")

def display_all_notes(filename: str = "notes.json") -> None:
    """Display all notes"""
    notes = load_notes(filename)
    if not notes:
        print("No notes found.")
        return
    
    for note in notes:
        display_note(note)

def get_all_tags(filename: str = "notes.json") -> List[str]:
    """Get all unique tags from notes"""
    notes = load_notes(filename)
    all_tags = set()
    for note in notes:
        all_tags.update(note['tags'])
    return sorted(list(all_tags))

def get_note_count(filename: str = "notes.json") -> int:
    """Get total number of notes"""
    return len(load_notes(filename))

# Export and Import Functions
def export_to_text(filename: str = "notes.txt", source_file: str = "notes.json") -> None:
    """Export all notes to a text file"""
    notes = load_notes(source_file)
    
    with open(filename, 'w') as f:
        for note in notes:
            f.write(f"Title: {note['title']}\n")
            f.write(f"Date: {note['created_at']}\n")
            f.write(f"Tags: {', '.join(note['tags'])}\n")
            f.write(f"Content:\n{note['content']}\n")
            f.write("-" * 50 + "\n\n")

def backup_notes(backup_file: str = "notes_backup.json", 
                 source_file: str = "notes.json") -> None:
    """Create a backup of all notes"""
    notes = load_notes(source_file)
    with open(backup_file, 'w') as f:
        json.dump(notes, f, indent=4)
    print(f"Backup created: {backup_file}")

# Advanced Features
def add_tag_to_note(note_id: int, tag: str, filename: str = "notes.json") -> bool:
    """Add a tag to an existing note"""
    notes = load_notes(filename)
    
    for note in notes:
        if note['id'] == note_id:
            if tag not in note['tags']:
                note['tags'].append(tag)
                note['updated_at'] = datetime.now().isoformat()
                save_notes(notes, filename)
            return True
    return False

def remove_tag_from_note(note_id: int, tag: str, filename: str = "notes.json") -> bool:
    """Remove a tag from a note"""
    notes = load_notes(filename)
    
    for note in notes:
        if note['id'] == note_id:
            if tag in note['tags']:
                note['tags'].remove(tag)
                note['updated_at'] = datetime.now().isoformat()
                save_notes(notes, filename)
            return True
    return False

def merge_notes(note_id1: int, note_id2: int, filename: str = "notes.json") -> Optional[Dict]:
    """Merge two notes into one"""
    notes = load_notes(filename)
    note1 = None
    note2 = None
    
    for note in notes:
        if note['id'] == note_id1:
            note1 = note
        if note['id'] == note_id2:
            note2 = note
    
    if note1 and note2:
        merged_note = {
            'id': len(notes) + 1,
            'title': f"{note1['title']} & {note2['title']}",
            'content': f"{note1['content']}\n\n---\n\n{note2['content']}",
            'tags': list(set(note1['tags'] + note2['tags'])),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        
        # Remove original notes and add merged
        notes = [n for n in notes if n['id'] not in [note_id1, note_id2]]
        notes.append(merged_note)
        save_notes(notes, filename)
        return merged_note
    
    return None

def clear_all_notes(filename: str = "notes.json") -> None:
    """Delete all notes (with confirmation)"""
    confirm = input("Are you sure you want to delete ALL notes? (yes/no): ")
    if confirm.lower() == 'yes':
        save_notes([], filename)
        print("All notes deleted.")
    else:
        print("Operation cancelled.")

# Statistics Functions
def get_note_statistics(filename: str = "notes.json") -> Dict:
    """Get statistics about notes"""
    notes = load_notes(filename)
    
    if not notes:
        return {"total_notes": 0}
    
    total_chars = sum(len(note['content']) for note in notes)
    avg_length = total_chars / len(notes)
    
    tag_counts = {}
    for note in notes:
        for tag in note['tags']:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    
    return {
        "total_notes": len(notes),
        "total_characters": total_chars,
        "average_note_length": avg_length,
        "unique_tags": len(tag_counts),
        "most_common_tag": max(tag_counts, key=tag_counts.get) if tag_counts else None,
        "tag_distribution": tag_counts
    }