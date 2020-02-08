import random
import string

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave', 'aggressive', 'agreeable', 'ambitious', 'chubby', 'clean', 'dazzling', 'elegant', 'fancy', 'flabby', 'glamorous', 'gorgeous', 'long', 'magnificent', 'muscular', 'plain', 'quaint', 'scruffy', 'shapely', 'short', 'skinny', 'stocky', 'unsightly', 'breakable', 'bright', 'busy', 'calm', 'Careful', 'Cautious', 'Cheerful', 'clear', 'Clever', 'Colorful', 'Clumsy', 'funny', 'Open', 'crazy', 'Perfect', 'Wild', 'Healthy', 'Healthy', 'Helpful', 'Crowded', 'Confused', 'Concerned', 'Comfortable', 'Gifted', 'Gentle', 'Friendly', 'nice', 'Tough', 'Tired', 'Mysterious', 'Famous', 'Modern', 'Expensive', 'Lucky', 'Kind', 'Average', 'easy', 'Annoyed', 'Rich', 'real', 'fake', 'Impossible', 'Angry', 'Amused', 'late', 'terrified', 'Important', 'Different', 'Delightful', 'Adventurous', 'Shiny', 'Innocent', 'Silly', 'Smiling', 'Sore', 'Sparkling', 'Jolly', 'Stormy', 'Successful', 'Super', 'Talented', 'Tasty', 'Thoughtful', 'Thankful', 'Motionless', 'Misty', 'Foggy', 'Fantastic', 'Terrific', 'Cloudy', 'Pickled', 'Salty', 'Spicy', 'Slimy', 'Soft', 'Smooth', 'Slippery', 'Solid', 'Icy', 'Hot', 'Hard', 'Fuzzy', 'Silky', 'Sharp', 'Cold', 'Freezing', 'Sticky', 'Chilly', 'Melted', 'Warm', 'Silent', 'Quiet', 'Noisy', 'Loud', 'Whispering', 'Voiceless', 'Thundering', 'Squeaking', 'Golden', 'Small', 'Tall', 'Giant', 'Huge', 'Massive', 'Narrow', 'Wide', 'Hollow', 'Deep', 'Curved', 'Steep', 'Straight', 'Triangular', 'Circular', 'Round', 'Rainy']

nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'banana', 'duck', 'panda', 'ocean', 'mountain', 'train', 'flower', 'building', 'house', 'tower', 'light', 'phone', 'book', 'clock', 'speaker', 'sun', 'bed', 'movie', 'snow', 'water', 'rain', 'food', 'music', 'monkey', 'elephant', 'telephone', 'teacher']

print('Welcome to Password Picker!')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    
    password = adjective + noun + str(number) + special_char
    print('Your new password is : %s' % password)
    
    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
        break