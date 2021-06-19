label r1_movie:
    # Go to the movie
    #
    # Music: Happy excited, doesn’t loop, > 3 minutes (same as before)
    # Background: Cinema
    #
    # They arrived at the cinema. Saw there were two movies that were playing today.
    # One was horror and the other was romance.
    # “Shiraishi, which one do you want to watch?”
    # “I’ll leave it to Hitona neechan~”.
    # So it’s obvious which one right?

    "I paid the meal then we went out to a cinema"

    p "I paid the meal then we went out to a cinema"
    
    p "You’ve been to a cinema right Shiraishi?"

    s "No, Shiraishi never been to a cinema before"

    p "Really? Then Hitona nee-chan here will make this your best cinema experience ever!"

    s "Yaaay"

    "From the looks of it, there are two movies playing…"

    "Horror movie and a romance movie"

    p "Shiraishi, which one do you want to watch?"

    s "I’ll leave it to Hitona nee-chan"

    menu:
        "Looking at the selection it’s pretty obvious which one we’re watching right?"
        
        "Horror Movie":
            "I bought the ticket, and not long after it was time for the movie"
            
            "The movie name is ParanormalJP"
            
            "The movie synopsis said it's about some people challenging a Haunted Street where they need to get out"
            
            "At first it was just a game while they were recording it but it became something more..."
            
            "Well we'll see how it is"
            
            p "If you're scared Shiraishi you can close your eyes or hold my hands okay"

            s "Okay~"

            "The movie is starting"

            "It's quite dark as well, expected from a horror movie"

            "Oh the movie is from a first person perspective as the cameraman, interesting"

            "Cathy is her partner, looks like they'll be together"

            "I looked at Shiraishi she seemed fine"

            "Cathy" "Come on let's go...AAAAAH HELP ME"

            "Cathy is being dragged by something..."

            "Now the cameraman is alone..."

            "I don't want to watch anymore..."

            "Shiraishi held my hand, is she scared?"

            "I got to hold on until the end then, let's go..."

            "The movie ended"

            s "That was fun!!"

            p "It was?? I see...good then"

            "So Shiraishi was just comforting me. What a strong and good girl"

            "I gave her a head pat"

        "Romance Movie":
            "The movie name was Nakitai Watashi wa Same wo Kaburu"

            "The movie synopsis said it's about someone who wanted to run away from her usual life."

            "She met a strange character then she managed to become a…?"

            "Well we'll see how it is"

            p "This should be fun Shiraishi"

            s "Shiraishi can't wait!"

            "The movie is starting"

            "Oh here is the main character, she's a middle schooler huh"

            "What a strong minded this girl is keeps getting close to her crush even though he's not"

            "responding much to her"

            "Ooh such a backstory this girl have..."

            "The strange character is here! It's a...fish in an aquarium"

            "The fish gave her a mask"

            "She jumped to the ocean!?? Put on the mask and now she's...a shark...I see"

            "Shiraishi seemed to be enjoying it, well let's watch till the end"

            "The movie ended"

            s "That was fun!!"

            p "Yeah that was nice~ Good you enjoyed it too"

            "I gave her a head pat"
        
    # Shiraishi then asked “Would you watch a movie again someday?”.
    # Surely you know what to say

    s "Hitona nee-chan, would you watch a movie with me again someday?"

    menu:
        "What’s with the sudden question? Well…"
        "i don't know":
            jump r1_movie_bad_end
        "definitely":
            jump r1_after_movie
