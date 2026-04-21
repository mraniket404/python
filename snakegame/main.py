import random
import time
import sys

class SnakeWaterGun:
    def __init__(self):
        self.choices = {
            's': {'name': 'Snake', 'icon': '🐍', 'beats': 'w'},
            'w': {'name': 'Water', 'icon': '💧', 'beats': 'g'},
            'g': {'name': 'Gun', 'icon': '🔫', 'beats': 's'}
        }
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
    
    def display_header(self):
        """Display game header"""
        print("\n" + "=" * 50)
        print("     SNAKE 🐍  WATER 💧  GUN 🔫")
        print("=" * 50)
        print(f"Score: You {self.player_score} : {self.computer_score} Computer")
        print("-" * 50)
    
    def get_computer_choice(self):
        """Get random choice for computer"""
        return random.choice(list(self.choices.keys()))
    
    def determine_winner(self, player, computer):
        """Determine winner of a round"""
        if player == computer:
            return "tie"
        
        if self.choices[player]['beats'] == computer:
            return "player"
        else:
            return "computer"
    
    def display_round_result(self, player_choice, computer_choice, winner):
        """Display round results with animation"""
        print(f"\nYou chose: {self.choices[player_choice]['icon']} {self.choices[player_choice]['name']}")
        print(f"Computer chose: {self.choices[computer_choice]['icon']} {self.choices[computer_choice]['name']}")
        
        time.sleep(0.5)
        print("\n" + "-" * 30)
        
        if winner == "tie":
            print("🤝 IT'S A TIE! 🤝")
        elif winner == "player":
            print(f"🎉 {self.choices[player_choice]['name']} beats {self.choices[computer_choice]['name']}! YOU WIN! 🎉")
        else:
            print(f"💻 {self.choices[computer_choice]['name']} beats {self.choices[player_choice]['name']}! COMPUTER WINS! 💻")
    
    def play_round(self):
        """Play a single round"""
        while True:
            print("\nYour options:")
            for key, value in self.choices.items():
                print(f"  {key} - {value['name']} {value['icon']}")
            print("  q - Quit game")
            
            player_input = input("\nEnter your choice: ").lower().strip()
            
            if player_input == 'q':
                return False
            
            if player_input in self.choices:
                computer_choice = self.get_computer_choice()
                winner = self.determine_winner(player_input, computer_choice)
                
                self.display_round_result(player_input, computer_choice, winner)
                
                if winner == "player":
                    self.player_score += 1
                elif winner == "computer":
                    self.computer_score += 1
                
                self.rounds_played += 1
                return True
            else:
                print("❌ Invalid choice! Please try again.")
    
    def display_final_results(self):
        """Display final game statistics"""
        print("\n" + "=" * 50)
        print("GAME SUMMARY")
        print("=" * 50)
        print(f"Total Rounds Played: {self.rounds_played}")
        print(f"Final Score - You: {self.player_score} | Computer: {self.computer_score}")
        
        if self.player_score > self.computer_score:
            print("\n🏆 CHAMPION! You defeated the computer! 🏆")
        elif self.computer_score > self.player_score:
            print("\n🤖 COMPUTER WINS! Better luck next time! 🤖")
        else:
            print("\n🤝 GAME TIED! Well played! 🤝")
        
        print("=" * 50)
    
    def run(self):
        """Main game loop"""
        print("\n🐍💧🔫 WELCOME TO SNAKE-WATER-GUN! 🔫💧🐍")
        print("\nRULES:")
        print("  • Snake drinks Water → Snake wins")
        print("  • Water damages Gun → Water wins")
        print("  • Gun kills Snake → Gun wins")
        print("\nPress Enter to start playing...")
        input()
        
        while True:
            self.display_header()
            if not self.play_round():
                break
        
        self.display_final_results()
        print("\nThanks for playing! 👋")

# Run the game
if __name__ == "__main__":
    game = SnakeWaterGun()
    game.run()