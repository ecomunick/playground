def hello(name, age):
    print("Hello, " + name +"! You are my " + str(age) + " years old beloved.")

hello("Tapioca", 17)

def talk(phrase):
    def say(word):
        print(word)

words = phrase.split(' ')
for word in words:
    say(word)

#talk('I\'am going to buy milk')

condition = True
while condition == True:
    print('The condition is True')
condition = False