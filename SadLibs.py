

adjlist = []
advlist = []
nounlist = []
verblist = []
numlist = []
propnounlist = []
gerrundlist = []



wordlists = [adjlist, advlist, nounlist, verblist, numlist, propnounlist, gerrundlist]

#storylist = []

def SelectStory():
    storyselection =(input("Which story would you like to experience? " + '\n' +
                           "Safari Adventure! (1)" + '\n' +
                           "Kingdom in Strife (2)" + '\n' +
                           "Enter the number of your desired story: " ))
    StartSadLib(storyselection)
    

def DeGerrunder(gerrund):
    newverb = gerrund[:-3]
    verblist.append(newverb)
    return

def StartSadLib(storyselection):
    story = ''

    if storyselection == '1':
        propnounlist.append(input("Give me a person's name: "))
        propnounlist.append(input("Give me another person's name: "))
        propnounlist.append(input("Give me one last person's name: "))
        adjlist.append(input("I need an adjective: "))
        adjlist.append(input("Another adjective please: "))
        verblist.append(input("Now a verb: "))
        adjlist.append(input("Gimme an adjective: "))
        numlist.append(input("A number please: "))
        nounlist.append(input("A plural animal: "))
        gerrundlist.append(input("A verb ending in -ing: "))
        advlist.append(input("An adverb: "))
        nounlist.append(input("A natural environment: "))
        verblist.append(input("Another verb: "))
        advlist.append(input("An adverb: "))
        adjlist.append(input("I need an adjective now: "))
        adjlist.append(input("An adjective: "))
        nounlist.append(input("A plural article of clothing: "))
        adjlist.append(input("An adjective: "))
        nounlist.append(input("A noun: "))
        verblist.append(input("Another verb: "))
        adjlist.append(input("Another adjective: "))
        adjlist.append(input("An adjective: "))
        advlist.append(input("An adverb: "))
        adjlist.append(input("An adjective: "))

        story = '\n' + propnounlist[0] + ", " + propnounlist[1] + ", and " + propnounlist[2] + \
         " are all going on an adventure. " + propnounlist[0] + " is the leader of the " + adjlist[0] + " crew. " + propnounlist[1] + \
         " is the " + adjlist[1] + " one, and " + propnounlist[2] + " is the most likely to " + verblist[0] + ". As the " + adjlist[0] + \
         " crew treks their way through the " + adjlist[2] + " wilderness, " + propnounlist[2] + " notices a group of " + numlist[0] + " " + nounlist[0] + \
         ". They were " + gerrundlist[0] + " " + advlist[0] + " across the " + nounlist[1] + ". " + propnounlist[1] + " whispers to the others, 'We should " + verblist[1] + \
         " them " + advlist[1] + " before they get away! " + propnounlist[0] + " agrees, but as s/he moves in to " + verblist[1] + \
         " s/he is stopped by " + " a " + adjlist[3] + " looking man, all dressed in " + adjlist[4] + " " + nounlist[2] + " and brandishing a " + adjlist[5] + \
         " " + nounlist[3] + ". He gesturs toward the " + nounlist[0] + " and shakes his head. " + propnounlist[1] + " leans in to the group and says, 'I think this " + adjlist[3] + \
         " fellow doesn't want us to " + verblist[1] + " these " + nounlist[0] + ". Perhaps we should try to" + verblist[2] + \
         " them instead? " + propnounlist[2] + " nods in agreement, stepping forward to " + verblist[2] + " the " + nounlist[0] + ". The " + nounlist[3] + \
         " wielding man nods in approval. He gestures for the group to follow." + " He leads the group to a " + adjlist[6] + " hidden village, with a statue of " + nounlist[0] + \
         " in the center. The group's guide calls out and gathers the villagers. Each one carrying something " + adjlist[7] + " and laying it " + advlist[2] + \
         " at the base of the statue." + "Then, all eyes turn to the group. The village raises their voices and sings a " + adjlist[8] + " song. When the song ends, they gather all the " + adjlist[7] + \
         " things and give them to the group. With that, " + propnounlist[2] + " says, 'What a great adventure guys! This makes me feel like going for a " + verblist[0] + \
         "." + '\n'
    elif storyselection == '2':
        propnounlist.append(input("A name: "))
        propnounlist.append(input("Your favorite country: "))
        nounlist.append(input("A plural noun: "))
        adjlist.append(input("An adjective: "))
        verblist.append(input("A verb: "))
        nounlist.append(input("A plural animal: "))
        adjlist.append(input("An adjective: "))
        advlist.append(input("An adverb: "))
        verblist.append(input("A verb: "))
        adjlist.append(input("An adjective: "))
        adjlist.append(input("An adjective: "))
        adjlist.append(input("An adjective: "))
        propnounlist.append(input("A pet's name: "))
        verblist.append(input("A past-tense verb: "))
        advlist.append(input("An adverb: "))
        adjlist.append(input("An adjective: "))
        advlist.append(input("An adverb: "))
        advlist.append(input("An adverb: "))
        nounlist.append(input("A noun: "))
        verblist.append(input("A past-tense verb: "))
        nounlist.append(input("A body part: "))
        advlist.append(input("An adverb: "))
        
        advlist.append(input("An adverb: "))
        adjlist.append(input("An adjective: "))
        nounlist.append(input("A kind of food: "))


        story = '\n' + propnounlist[0] + " was the prince/ss of " + propnounlist[1] + \
        ". S/he loved his/her kingdom more than " + nounlist[0] + ". Sadly, " + \
        propnounlist[1] + " was plagued by " + adjlist[0] + " monsters, who loved to " + \
        verblist[0] + " the villagers' " + nounlist[1] + ". " + propnounlist[0] + \
        " was so distressed s/he sent out a request for any " + adjlist[1] + \
        " knights who could " + advlist[0] + " " + verblist[1] + " the monsters. " + \
        "Many " + adjlist[2] + " knights answered his/her call, but none who could " + \
        verblist[1] + " the monsters " + advlist[0] + " enough. After months of waiting, " + \
        propnounlist[0] + " decided the time had come to take " + adjlist[3] + " action. " + \
        "S/he saddled up his/her " + adjlist[4] + " steed, " + propnounlist[2] + " and rode " + \
        "out to meet the leader of the monsters. When s/he arrived in the monsters' camp, all " +\
        "the monsters tried to " + verblist[0] + ' ' + propnounlist[2] + ", but " +\
        propnounlist[0] + ' ' + verblist[2] + " them all " + advlist[1] + \
        ". With the monsters rebuffed, " + propnounlist[0] + " demanded to speak with their " + \
        adjlist[5] + " leader, who stepped " + advlist[2] + " from his tent. " + \
        propnounlist[0] + " told him that s/he'd let them stay in " + propnounlist[1] + \
        " if they promised to stop " + verblist[0] + "ing the villagers' " + nounlist[1] + \
        ". The leader laughed " + advlist[3] + " and swung his " + nounlist[2] + " at " + \
        propnounlist[0] + " but s/he " + verblist[3] + " the " + nounlist[2] + \
        " rendering the leader powerless. Then, " + propnounlist[0] + " grabbed the leader's " + \
        nounlist[3] + " and twisted it " + advlist[4] + \
        ". The monsters' leader relented " + advlist[5] + " and asked if he and his people " + \
        "could share a meal to cement the truce. " + propnounlist[0] + " agreed, and they all enjoyed a " + \
        adjlist[6] + " meal of " + nounlist[4] + ". " + '\n'
        
         
    print (story)
    done = input("Would you like to play again? (Y/N)")
    
    if done == 'Y' or done == 'y':
        for list in wordlists:
            list.clear()

        print ('\n')
        SelectStory()
    else:
        done = 'N'
        
SelectStory()


