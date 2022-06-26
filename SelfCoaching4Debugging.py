## Program to walk a programmer through the mental process of Finding a Bug
# input key and suggestion library
# Used to move through the suggestions list
step = 0

# list to compare against input and exit the suggestion loop
foundit = ('foundit','FoundIt','FoundIt!','foundit!', 'gotit', 'Gotit!', 'GotIt')

suggestions = ["""Let's start with trouble shooting the human part of this puzzle.\n
            Have you taken a brain break in the last hour?
            Have you drunk water, eaten food or gone to the washroom recently?\n
            If the answer is no to any of these factors,
            take a timed break and go take care of your body.
            You'll come back being able think better.
            When you return, type any key + enter\n""",
            """Let's start with the basics.\n
            Are your variables in order?\n
            Are they well named, specific and accurate?\n
            Go trough each one; this stuff can be confusing and that's okay.\n""",
            """            Is there a way you can make it simpler or cleaner?\n
            Sometimes figuring out how to map programs takes a while and that's okay.\n
            Remember to breathe.\n""",
            """            Am I useing the correct tools for the job?\n
            There are so many tools!\n
            It can be a process to figure out what the right one is.\n""",
            """            Do you have print statements at important key points?\n
            Take a moment and assess what you need to know.\n
            It's okay that you don't know it yet; ask the computer for what you can.\n""",
            """            Do you know at what point the program is malfunctioning?\n
            Computers and humans think differently; it's okay that it's taking time to figure it out.\n""",
            """            Does the flow of your code match your intent?\n
            Figuring out the flow is a process.\n
            It's okay if you haven't gotten it yet.\n""",
            """            How is the computer creating the results?\n
            What instructions create that pattern?\n
            Pattern recognition takes time. Remember to breathe.\n""",
            """            How is the computer misunderstanding your code?\n
            How are you misunderstanding the computer?\n
            It's okay; you're learning how to communicate with a computer and that's amazing.\n""",
            """            What information would make this work better and how can I find it?\n
            There's no way to know everything; but knowing when to get more information is a god-tier-skill.\n""",
            """            Is there a tool I should research to confirm I'm using correctly?\n
            There are so many tools; it's okay if you're not fluent with everything you're using.\n""",
            """            How are things working correctly?\n
            Knowing what's working well is half the battle.\n""",
            """            Be social with your Rubber Ducky\n
            Verbally explain or write a letter outlining your code and what's not working right.\n
            Sometimes we need to externally process what's happening, and that's okay.\n""",
            """            What could I do in a different way?\n
            You're using the tools you intiially thought were the best tactic.\n
            It's okay if you need to change directions.\n""",
            """            What haven't I considered yet?\n
            There are always more options; be kind with yourself as you consider them.\n""",
            """            If I did ask for help, can I guess what they would say?\n
            It's okay to ask for help... and sometimes guessing the advice they'd give is more accessible.\n""",
            """            What resources would be the best place to find help, right now?\n
            Knowing how to get help is super valuable and it's great that you're thinking about it.\n""",
            """            How could I prepare to ask for help?\n
            Going into asking help knowing what you want to ask, with screen shots, etc can make it more comfotable to ask for help.\n""",
            """If you've gotten this far without success, it's time to take a break bio break and come back to this later.\n
            Ask yourself how you could approach this differently.\n
            Be sure to appreciate the amount of effort and thought you've put into this problem.\n"""]

# Helping client to know what the process of the program is
reply = str(input("""Okay, let's figure out together how to help you find the bug.
We'll go through a series of questions to help you problem solve.

If you haven't done a suggestion, go use the suggested technique to find your bug!
If it works, type 'FoundIt!' + enter to exit the question section.
When you have tried the suggestion and not gained the desired result,
hit any key + enter to continue to the next suggestion.

Remember to breathe;  you're doing something difficult.
It's okay that it takes time!\n
When you're ready, hit any key + enter'\n"""))


# Looping through the questions until the client replies next
for n in suggestions:
        print(suggestions[step])
        reply = input("Type any key + enter when you're ready to look at the next suggestion.\nSay 'FoundIt!' to exit the suggestion loop\n")
        # If the user finds the solution, this is how they exit the while loop
        if reply in foundit:
                #print("Congratulations, you found a solution!")
                break
        step = step + 1


print("""Congratulations, you found a solution!
      Remember to pat yourself on the back
      Celebrate figuring it out
      And *thank yourself for the hard work* you've put in learning how to do this!

      Also, step away from the computer and enjoy the sensation of having found the bug
      You deserve it!""")