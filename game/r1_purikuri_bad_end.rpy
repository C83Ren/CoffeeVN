label r1_purikuri_bad_end:

    #no BGM
    
    "I looked at the photo, but it was still black."

    p "(Ah, it’s starting to get clearer now! I can see it!)"

    "The photo started to get more and more clear."

    p "(Huh…?)"

    "…"
    
    "…"
    
    #phone_call tone
    
    "{i}Ring ring ring{/i}"
    
    "It’s the sound of my phone ringing."

    "While still looking at the photo, I took out my phone."

    scene bg black

    "..."

    scene bg room
    
    "When I opened my eyes, I was lying on my bed."

    p "What…was that…"

    #phone_call tone

    "{i}Ring ring ring{/i}"

    "My phone is ringing."

    "It’s from senpai."

    sn "Kohiii! Morning~! So about today…"

    sn "…"

    sn "…"

    p "Oh, okay, I see. See you then."

    "I hung up."

    p "Guess I’ll go stream or something then."
    
    jump end_2

label end_2:

    scene bg black

    "bad end"
    $ persistent.ed_unlocked_2 = True
    return
