
l = [1, 2, 3, 4, 5]  # ye ek list hai jisme 1 se 5 tak ke numbers hain

square = lambda x: x * x # ye lambda function hai jo ek argument leta hai aur uska square return karta hai
squared_list = list(map(square, l)) # map function ka use karke humne list ke har element ko square kiya hai
print(squared_list) # ye squared list ko print karta hai

#filter function ka use karke humne list ke har element ko check kiya hai ki kya wo even hai ya nahi
even_list = list(filter(lambda x: x % 2 == 0, l)) # ye filter function ka use karke humne list ke har element ko check kiya hai ki kya wo even hai ya nahi
print(even_list) # ye even list ko print karta hai  

#reduce function ka use karke humne list ke har element ko add kiya hai
from functools import reduce # reduce function ko use karne ke liye hume functools module ko import karna padta hai
sum = reduce(lambda x, y: x + y, l) # ye reduce function ka use karke humne list ke har element ko add kiya hai
print(sum) # ye sum ko print karta hai