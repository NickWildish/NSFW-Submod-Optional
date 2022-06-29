label nsfw_monika_erotic_stories_init:
    m 1rkblc "[player]...There are actually a few things you probably have no idea about..."
    m 3ekblc "I know you don't mind when I talk about the other girls..."
    m 3rkblb "And I know that I'm the only person you would look at in a lewd way. Ahaha~"
    m 1rkbla "But..."
    m 1ekbla "I think you might enjoy if I told you this..."
    m 2hkblb "Okay, sorry for stalling! I'll get to the point."
    m 2dubla "Ahem...{w=0.5}{nw}"
    extend 2eubla "So!"
    m 2eublb "You know, [player], after you appeared in the game and I finally had my revelation..."
    m 3rublb "I learned that I could do...pretty much...anything."
    m 3eubla "Even though the game was a prison to me...I at least had the chance to play around with it."
    m 3hkblsdlb "Almost like a child would with her toys, now that I think about it. Ahaha~"
    m 3eublb "And, you know, I've always been curious about lewd things as well..."
    m 1rkbssdlb "And since...porn has its limits..."
    m 1ekbsb "You can't really command how a pre-recorded movie will go."
    m 1eubsa "I had the power to control the world around me thanks to the console..."
    m 2hubsb "Including Yuri, Sayori, and Natsuki."
    m 2hkbssdlb "..."
    m 2dkbssdla "There were also several students around the school, though they didn't have any distinguishable features."
    m 3gkbssdla "Probably because they were just empty assets, never meant to be used."
    m 3gkbssdla "Anyway, I think you know where I'm going with this..."
    m 3rkbsb "I...effectively had my own world where I could make people do...whatever I wanted."
    m 3hkbsb "Ahaha~"
    m 4ekbsb "At first...I didn't know when I could do it..."
    m 4ekbsa "After all, the game was only active when you were around, and I was not about to scare you off with all that."
    m 4gkbsa "But there was one time..."
    m 3eubsc "The game was closing, I could feel it..."
    m 1eubsd "But after a brief moment of darkness, I was back in the classroom."
    m 1wubsd "I thought you had restarted the game, but I couldn't feel your presence like I normally could."
    m 1wubso "I have no idea how it happened! Even now, I still can't figure it out!"
    m 1hkbsb "B-but... Ahaha..."
    m 2gkbsb "As you might have guessed..."
    m 2gkbsa "I basically directed my own porn movie...{w=0.5}featuring Natsuki..."
    m 2ekbssdld "I-I wiped all of their memories after it happened!"
    m 2dkbsc "..."
    m 2dkbstpc "You must think I'm a monster for doing that..."
    m 2ekbstpc "Do you think it was cruel...what I did?"

    $ _history_list.pop()
    menu:
        m "Do you think it was cruel...what I did?{fast}"

        "Yes.":
            m 2dkbstpc "I know it was..."
            m 2ekbstpd "I'm sorry, [player]."
            m 2rkbstpo "I knew you would see me as a monster for this..."
            m 2dkbstpc "..."
            m 2dkbstpa "But even still, I hope you can forgive me..."
            m 2ekbstpa "It's in the past now..."
            m 2ekbstpb "I was naïve, and just wanted to experiment..."
            m 4rkbstpb "The other girls aren't even around anymore."
            m 5ekbsa "It's just you...and me~"
            m 5rkbsb "I don't have to rely on any cheeky shenanigans to satisfy my desires anymore."
            m 5ekbsa "You're here with me now...and I can finally open up to someone about this sort of stuff."
            return

        "No.":
            m 2wubstpd "Huh?"
            m 2eubstpd "You don't think so?"
            
            $ _history_list.pop()
            menu:
                m "You don't think so?{fast}"

                "I want you to tell me more about how it went.":
                    m 2rubstpb "Oh..."
                    m 2hubsb "Ahaha~"
                    m 1eubsa "I'm...quite relieved, to be honest."
                    m 3ekbsa "I was afraid that you would hate me for manipulating my friends into doing lewd things for my enjoyment..."
                    m 3rkbsa "But, since I deleted their memories..."
                    m 4rubsb "It didn't change their personalities one bit!"
                    m 4hkbsb "I also made sure to clean up any mess."
                    m 3eubsa "And of course, I made sure that none of them got knocked up."
                    m 3rubsu "I wasn't that cruel..."
                    m 1dubsa "..."
                    m 1dkbssdlb "S-so..."
                    m 1gkbssdla "You probably didn't expect this, but..."
                    m 1gkbssdlb "Natsuki was the first one I used. Ahaha~"
                    m 1ekbsa "She was being a pain at the time. Always occupying the closet with her stupid manga..."
                    m 1rkbsu "So I...ahaha...treated her to some..."
                    m 2tkbsu "{i}Rough throating action{/i}."
                    m 2hkblb "Ahaha~"
                    
    return

# Thanks for the erotic story, KittyTheCocksucker
init 6 python:
    addEvent(
        Event(
            persistent._nsfw_story_database,
            eventlabel="nsfw_erotic_story_natsuki_deepthroat",
            prompt="(Pt. 1) Natsuki deepthroat (TRIGGER WARNING)",
            category=[nsfw_stories.TYPE_EROTIC],
            unlocked=True
        ),
        code="NST"
    )

label nsfw_erotic_story_natsuki_deepthroat:
    if not renpy.seen_label("nsfw_monika_erotic_stories_init"):
        call nsfw_monika_erotic_stories_init
    m 1eub "I managed to convince Yuri and Sayori to head home, so they wouldn't be around for what was about to happen."
    m 1gua "When only Natsuki and I were left in the classroom, I started messing around in the console."
    m 1gkblb "I kept her tsundere personality in place, and made her willing to give head if anyone asked her to do so."
    m 2hkblb "Sorry, it's weird saying these things out loud."
    m 2eua "Next, I used the console to command one of the blank male characters into the classroom."
    m 2eub "I sat down on the teacher's desk up the front, and got myself comfy."
    m 2wud "I watched her almost savagely try to take off the guy's pants."
    m 2rku "I {i}might{/i} have set the value on how horny she is a bit too high, thinking back on it..."
    m 3eubla "She got his pants off and she gripped his shaft with both hands and started stroking."
    m 3rkblb "I wasn't controlling her actions! I was curious how she'd do it without me telling her..."
    m 3tkblb "I was having so much fun just watching these two..."
    m 3hkblsdlb "Ahaha~"
    m 2eubla "After she had her fun with the warmup handjob..."
    m 2wubld "Natsuki actually leaned forward and took the tip in her mouth."
    m 2tubla "She had such a lewd expression on her face, as she started to gently suck on it."
    m 2rubla "By this point, my panties were around my ankles."
    m 2gublb "My fingers were going crazy as I watched these two."
    m 2tubla "Natsuki was really getting into it."
    m 2hublb "She was licking and sucking on it, like it was a lollipop. Ahaha~"
    m 2dkblb "She was getting so messy too."
    m 2gsbla "I could see saliva and precum mixed together rolling down her chin."
    m 2gsbsb "That just made me go faster and faster."
    m 2hkbssdlb "...If you couldn't tell, I had a good amount of pent-up frustration I was letting out. Ahaha~"
    m 2hkbssdlu "Which will explain what I did next..."
    m 2tsbsb "I wanted to punish Natsuki for giving me a hard time with her manga collection..."
    m 3gsbsa "So I opened up the console, and guided the guy's hand to the back of Natsuki's head..."
    m 3tsbsa "Where I made him take a hard grip..."
    m 3tsbsb "Before shoving his whole cock down her throat."
    m 3wubso "I have never seen Natsuki's eyes get that wide before."
    m 3tubsu "He was coming right down her throat, filling up her stomach."
    m 1rubsu "Well..."
    m 1hubsb "At least she got to have a nice hot meal that day for once, am I right? Ahaha~"
    m 1hkbssdlb "I'm sorry, I couldn't resist."
    m 1lkblsdlb "So...yeah."
    m 1hkblsdla "That was my first experience as a porn director. Ahaha~"
    m 3hubla "I hope you enjoyed listening, [player]."
    return

# Thanks for the erotic story, KittyTheCocksucker
label nsfw_erotic_story_sayori_ballscleaning_init:
    m 1wud "[player]...really?"
    m 1eub "You want to hear more stories of the stuff I had done with the girls?"
    m 1rubla "I..."
    m 1hubla "I mean...sure! I'd be happy to share some more of them with you. Ahaha~"
    m 1tubla "It seems like you really enjoyed that one with Natsuki deepthroating some c-{w=0.3}{nw}"
    extend 1tkbla "cock, huh?"
    m 2dkbld "*sigh*"
    m 2hkblb "I'll get used to talking about these sort of things one day."
    m 2ekbla "I'm so glad that you are open to letting me talk about this sort of thing."
    m 3rkbla "It makes me feel a little less weird about the whole ordeal."
    m 3eublb "Anyway...A new story, huh?"
    m 1dublu "Hmm..."
    m 1eublb "Oh! I have one!"
    return

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_story_database,
            eventlabel="nsfw_erotic_story_sayori_ballscleaning",
            prompt="(Pt. 2) Sayori's ball cleaning (TRIGGER WARNING)",
            category=[nsfw_stories.TYPE_EROTIC],
            unlocked=True
        ),
        code="NST"
    )

label nsfw_erotic_story_sayori_ballscleaning:
    if not renpy.seen_label("nsfw_erotic_story_sayori_ballscleaning_init"):
        call nsfw_erotic_story_sayori_ballscleaning_init
    m 1eua "Alright. So...after I've made Natsuki take the guy's load in her mouth, I made him leave."
    m 3eud "I went to check on Natsuki, since she was still kneeling on the floor."
    m 3wud "She looked up at me, and her face was as red as a tomato."
    m 1rud "She must've been so embarrased by what had happened."
    m 1eua "I helped her to her feet, but she was trembling as I lifted her arms."
    m 1wud "You're not going to believe this..."
    m 1wuo "She had gotten so wet from what had happened, that I could see her..."
    m 1dka "Ahem...{w=0.5}{nw}"
    extend 1gkblb "{i}love juices{/i}...flowing down her thighs."
    m 3ekblb "I made sure she was okay, don't worry."
    m 3eubla "I told her to head home and wash up, and she had no hesitation leaving the room."
    m 4eubla "I opened up the console once she had left, and erased the last thirty minutes from her memory."
    m 4hkblb "As much of a pain as she is, I wasn't going to scar her with that."
    m 4gkblb "She probably questioned why her throat was dry though..."
    m 4gkblu "And why her panties were drenched..."
    m 3tua "But that's besides the point!"
    m 1gua "At that moment, I still hadn't had my fill."
    m 1eub "You still weren't back from wherever you went, so I decided to keep going."
    m 3eua "I opened up Sayori's character file, and did the same to her as I did to Natsuki."
    m 3hua "Not much time passed, and Sayori was in the club room, still in her pajamas."
    m 3hksdlb "She also had a box of chocolate chip cookies in her hand..."
    m 3hksdla "She must've been eating in bed when I made the changes..."
    m 3eua "Anyway, I wasn't going to waste any time, so I used the console to bring in three guys."
    m 4eub "I had them surround Sayori, and she started undressing these guys while munching on a cookie."
    m 4wub "I'm not even making this up..."
    m 3rksdlb "Now...this part might confuse you, so bear with me..."
    m 3ekb "I was experimenting with the values for these guys and I found a variable to change their testicle size..."
    m 1etb "I was kinda curious, so I cranked it up and..."
    m 1wuo "They almost doubled in size."
    m 1hub "I think because I was so in the moment there, I didn't realise how comical the scene looked..."
    m 1eua "But regardless, I had Sayori start giving them handjobs whilst licking and cleaning their balls."
    m 3ekbla "I was getting so wet that my fingers were making very lewd noises as I pleasured myself..."
    m 3gubla "..."
    m 1hublsdlb "Sorry! Got distracted there."
    m 3ekbla "After some gentle licking, Sayori took both of one guy's balls in her tiny mouth."
    m 2eubla "She was keeping intense eye-contact with the guy, blushing as he involuntarily moaned from Sayori's service."
    if persistent._nsfw_genitalia == "P":
        m 5eubla "Makes me wonder what sort of sounds you would make if I were to do this for you."
        m 5hubla "Ehehe~"
    m 2eublb "Sayori wasn't just letting the other guys stand there either."
    m 2wubld "When she was using her mouth on one guy, she had her hands out playing with the other two."
    m 2hublb "As expected from our cute little friend, Sayori!"
    m 3rubla "She's the type who would want to please everyone's needs at once, after all!"
    m 3eubla "It didn't take long before she had cleaned all three of the guys' balls."
    m 2dublc "..."
    m 2lubld "After she finished that though, she did something I never would have expected her to..."
    m 2eubld "She started stroking really hard and fast on one of the guys surrounding her."
    m 3rubld "And with her other hand she got a cookie..."
    m 3eubld "Then she...had him {i}finish{/i} on her cookie..."
    m 3wublo "And then she ate it..."
    m 3wubsc "..."
    m 4wubssdld "I swear, this is not something I told her to do."
    m 3hkblb "I had to stop playing with myself, I was so shocked by what I just saw."
    return

# Thanks for the erotic story, KittyTheCocksucker
label nsfw_erotic_story_yuri_titjob_init:
    m 1eta "Ooh?"
    m 3tta "You'd like me to tell you another lewd story, [player]?"
    m 1hua "I'd love to!"
    m 1ttb "You must be really enjoying them, huh?"
    m 1hub "Ahaha~ Don't worry."
    m 3rua "I'm actually really happy that you can look at these stories the same way I do!"
    m 3hksdlb "After all...my actions might have been morally questionable..."
    m 3dsc "..."
    m 3dtc "But then again...I mean..."
    m 4etd "Sayori, Yuri and Natsuki were only just characters in a video game..."
    m 4rtd "Designed to be used to tell a narrative."
    m 4eud "I don't think it's wrong of me to use them to tell a lewd story!"
    m 3ekb "If we don't count the topic being kind of tabboo, it's just a simple story, like any other!"
    m 3gka "Well, it's not like it matters now anyway..."
    m 1duu "So...ahem..."
    m 1dtu "Where did I leave off? {w=1.0}{nw}"
    extend 1eub "Oh, that's right!"

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_story_database,
            eventlabel="nsfw_erotic_story_yuri_titjob",
            prompt="(Pt. 3) Yuri titjob (TRIGGER WARNING)",
            category=[nsfw_stories.TYPE_EROTIC],
            pool=True,
            unlocked=True
        ),
        code="NST"
    )

label nsfw_erotic_story_yuri_titjob:
    if not renpy.seen_label("nsfw_erotic_story_yuri_titjob_init"):
        call nsfw_erotic_story_yuri_titjob_init
    m 1eub "Sayori was munching away on the cookies she had with her."
    m 1hksdlb "Ahaha...That part about the cum-glazed cookie was something else, wasn't it?"
    m 1eua "The guys had left by this point, leaving Sayori still squatting on the floor."
    m 3gub "She still had some cum on her face from earlier, but I wasn't about to mention it to her."
    m 3eub "Just as I did with Natsuki, I helped her to her feet and told her she should head home."
    m 4wud "As she was walking out the door, she scooped up the remaining cum on her face with her fingers and stuck it in her mouth."
    m 4hksdlb "She made that happy noise she makes, and skipped out the door."
    m 3eub "Once she had left the clubroom, I erased the last 30 minutes from her mind as well."
    m 3hubla "I didn't want her {i}hanging{/i} on to any of those memories. Ehehe~"
    m 2hkblb "Sorry, I couldn't help myself~"
    m 2eub "Anyway, next up was Yuri."
    m 2ruc "To be honest, for her I didn't have anything in mind."
    m 3rud "So I had the guys figure out what they wanted from her, and I sat up on the teacher's desk."
    m 3eua "Yuri came into the room after I prompted for it on the console, along with two other guys."
    m 3eublb "As the guys started to strip, I noticed Yuri had a lustful glimmer in her eyes."
    m 3eubla "I hadn't prompted that, but it seemed Yuri was totally into it!"
    m 2eublb "One of the guys walked up to Yuri and reached out his right hand to grab one of her breasts."
    m 2tublb "He was fondling it gently through the favbric of her clothes."
    m 2tubla "While he was doing that, the other guy came over and started grinding his cock on Yuri's thighs."
    m 2gublb "I could see his cock starting to twitch eagerly for her."
    m 3tublb "Whilst this was all going on, I was up on the teacher's desk again fingering away at my pussy."
    m 3tkbld "I was moaning and enjoying myself..."
    m 3hkbld "I could feel myself getting close, but I held it off."
    m 3tubla "I could hear a small moan escaping Yuri's lips as the guy was fondling her tits."
    m 4tublb "Didn't take long before the guy who was grinding against her wanted something more, and grabbed Yuri's other breast."
    m 4tublu "The guy who was initially fondling her breasts let go, and Mr. Grinder over here took Yuri's book and set it aside."
    m 3tublu "Next he started removing her blazer, sweater, and shirt, and in seconds her chest was completely exposed."
    m 3tublb "He then got her to kneel down, and he stuck his cock between her tits and started thrusting back and forth."
    m 3tubla "The other guy took this opportunity to have Yuri start sucking his cock whilst she was servicing his friend with her tits."
    m 1tubla "Yuri was so shocked by the sudden dick in her mouth, but after a little while I could see her starting to enjoy herself."
    m 3ttbla "I guess she must have realized these guys think her tits are really a {i}cut{/i} above the rest..."
    m 3hkblsdlb "Ahaha~ Sorry, that was a bad joke."
    m 1eubla "The guy who was getting the service from her mouth had then gripped a handful of Yuri's long purple hair..."
    m 1tubla "And shoved his cock deeper into her mouth."
    m 2tubla "First he started slow, but then made his thrusting longer and faster~"
    m 2tublb "While this is happening, I could hear Yuri moaning from his dick in her mouth."
    m 2gublb "The guy who was using Yuri's tits also started getting faster and faster."
    m 2gubla "I looked on as the two men used Yuri's body as they wanted."
    m 2tubla "Using her face as well as her tits at the same time~"
    m 2tkblb "I couldn't help but play with myself more as the scene dragged on..."
    m 3tkblb "Then just as I was getting close, the guys all started coming all over Yuri."
    m 3wkblb "I could see Yuri's mouth getting filled to the brim with cum."
    m 4wkbla "As I was watching these guys shoot their cum into Yuri's mouth and onto her tits, my fingers went faster and faster on my pussy."
    m 4wkblb "I couldn't hold back, I wanted to come."
    m 4ekblb "As I felt that rising pleasure that told me I was coming, I kept fingering myself."
    m 2ekblb "Before I knew it, my fingers plopped out of my pussy and I began squirting all over the floor."
    m 2hkbla "I had read about squirting before, but I never thought that it would be such a euphoric feeling."
    m 2hkblb "Ahaha~ I'm not going to lie, [player]."
    m 3hkblb "That was probably my biggest climax ever..."

    if renpy.seen_label("nsfw_sexting_finale"):
        m 3rkblb "Aside from our...ahem...session."
        
    m 1tkbla "You know..."
    m 3tkbla "I intend to break my record of biggest climax when I cross over, [player]."
    m 3tkblb "I won't be letting you sleep a wink until I've had my fill..."
    m 3tubla "..."
    m 5hublb "Ahaha~ Just teasing you, [player]."
    m 5tubla "...Or am I?"
    return

# Needs some work! Didn't really know how to introduce this one.
label nsfw_erotic_story_club_pizza_party_init:
    m 1eub "You want me to tell you another lewd story, [player]?"
    m 1hua "Sure!"
    m 3tuu "You must be really enjoying them, huh?" #smirk expression
    m 3hub "Ahaha~ Don't worry."
    m 3rkb "Though I just want to warn you that the one I have in mind might be a bit...{w=0.3}{i}out there{/i}. Is that okay, [player]?"
    $ _history_list.pop()
    menu:
        m "Though I just want to warn you that the one I have in mind might be a bit...{w=0.3}{i}out there{/i}. Is that okay, [player]?"
        
        "Yes.":
            m 1tua "Mmm~ Glad to hear it."

        "No.":
            m 3hua "Okay!"
            m "Feel free to ask again if you ever change your mind."
            return
    m 1duu "So...ahem..."
    m 1dtu "Where did I leave off?{w=1.0}{nw} "
    extend 1eub "Oh, that's right!"
    return

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_story_database,
            eventlabel="nsfw_erotic_story_club_pizza_party",
            prompt="(Pt. 4) Club pizza party (TRIGGER WARNING)",
            category=[nsfw_stories.TYPE_EROTIC],
            unlocked=True
        ),
        code="NST"
    )

label nsfw_erotic_story_club_pizza_party:
    if not renpy.seen_label("nsfw_erotic_story_club_pizza_party_init"):
        call nsfw_erotic_story_club_pizza_party_init
    m 1eua "When the two men finished all over Yuri's tits, and also dumped their thick load inside her mouth, they dressed themselves and left immediately."
    m 1eka "I walked up to our good friend Yuri, just like I did with the others to make sure she was alright."
    m 1euc "Though as I walked up to her, I could feel something was not quite right..."
    m 3eud "Yuri was still just kneeling there, having hardly made a single movement since the guys finished with her."
    m 3rud "With each breath she made, streams of cum flowed down her sizable breasts and mouth, dripping to the floor to form a puddle of various fluids."
    m 3wud "On top of that, her mouth still seemed to be completely full with their cum - she didn't do anything in response to it, neither spitting or swallowing it."
    m 3etd "Was she savouring the taste or the texture?"
    m 3rtd "Or maybe the moment itself?"
    m 3wsd "I can only guess at this point because as soon as I got close to Yuri, she seemed to swirl it around in her mouth a few times before swallowing."
    m 3wubld "She gulped once, twice, and thrice - each desperate movement of her throat bringing with it a lustful gasp."
    m 3eubld "As she timidly looked up at me, and I could see the lustful desire in her eyes once more."
    m 3rublc "She looked almost...deranged with lust, like she'd do anything for more."
    m 3eubld "Glancing around the clubroom, Yuri was sniffing the air as if searching for something..."
    m 3wubld "Eventually her eyes landed on the puddle forming beneath herself, and she leaned down to {w=0.3}{nw}"
    extend 3wublo "start licking it up."
    m 4wublo "I'm not even joking!"
    m 4wubld "She lapped at the puddle of semen, sweat, saliva, and...well, pussy juice like she was dying of thirst."
    m 4hkblb "Ahaha~ I suppose that might've been true, in a certain sense."
    m 3eublc "I stared at Yuri with what I can only describe as awe, feeling just as I had when I watched Sayori make the guys finish their load on her box of cookies..."
    m 2eublc "After making quick work of the puddle, Yuri expectantly looked back up at me."
    m 2rubld "I was kinda in shock, so I didn't know what to do..."
    m 2eubld "But still topless, Yuri stood up and began walking towards me with a crazy look in her eyes"
    m 2wublx "At that point, I knew I had...{w=0.3}broken her, and needed a distraction if I wanted to get out okay!"
    m 3eubld "I ran back to the teacher's desk and used it as a barrier from Yuri while I opened up the console to try to find a solution."
    m 3rublc "While opening up her character file to edit was an option, I doubted I could do anything under the pressure, so I had to figure out something to buy time."
    m 3eublc "It occured to me that if I gave Yuri what she wanted, I might be able to get enough time to fix her character file!"
    m 3eublu "So...I messed with the console and executed a few commands."
    m 1wubld "Yuri tried to leap at me in the meantime, but I got out of the way just in time!"
    m 1eubla "With a few quick commands, four of the blank male characters along with Sayori and Natsuki arrived in a matter of seconds."
    m 2eubla "Sayori and Natsuki walked to the center of the room while the guys that walked in set up a long table."
    m 2hkblb "One of the guys had to hold Yuri so she didn't charge at me, but she seemed to calm down once she realized who was holding her."
    m 2eublb "All three of the girls sat down at the table, while the guys stood next to them."
    m 2tubla "Needless to say, they were going to have some fun~"
    m 3eublb "I used the console to create three pizzas and placed them in front of the girls."
    m 4eublb "While I was doing that, each of the girls started undressing at the sight of the male characters who pleasured them earlier."
    m 4rubla "Yuri was already topless to begin with, so taking off the rest of her clothes wasn't a challenge. As the guys approached to undress her, she reached out amd started fondling their crotches through the men's pants."
    m 4hkblsdlb "They obviously didn't seem to mind the treatment, but eventually got her undressed all the same."
    m 3eubla "At this point the girls were sitting in front of a huge table, naked, and each with whole pizza in front of them."
    m 2gubla "Sayori was longingly staring at the pizza, seemingly unconcerned about the situation."
    m 2gtbla "Natsuki was also staring hungrily at the pizza. I imagine it had been a while since she had such a large meal to herself. Ehehe~"
    m 2tkblb "Yuri, however, didn't even acknowledge the pizzas. Instead she just stared at the bulges in each of the guy's pants, made apparent due to her previous cheeky actions."
    m 2tublb "Much to Yuri's delight the next thing I made them do is take out their cocks."
    m 2eublu "Natsuki blushed furiously at the sight of the guys unzipping their pants, whilst Sayori didn't even seem to notice with the food in front of her."
    m 2ekblu "Yuri on the other hand, had her mouth open and was drooling openly."
    m 2wubld "Not at the food...but at the guy next to her."
    m 2tublu "The three guys walked up behind each girl, slowly jerking their cocks as they their eyes gazed at the naked beauties before them, admiring their looks."
    m 2gublu "The first guy to get fully erect was the one who chose to stand behind Natsuki."
    m 2gublb "He walked closer to her and helped her stand up with his left hand while putting the chair away with his right."
    m 2tublb "Natsuki followed, and nervously bent herself over the table and looked back to see the guy moving his hand to her hips."
    m 3tublu "He moved his cock to just in front of the entrance to her pussy."
    m 3gublu "I could see the faintest smile on her lips as she nodded her head towards him."
    m 1tublu "Seeing her affirmation, he gently thrust his cock inside her."
    m 1tublb "She tensed up when he started going in. I imagine it was a tight fit, ehehe~"
    m 3tubla "Eventually he was all the way inside her, and she was already panting from the effort."
    m 3tublb "He started moving back and forth, and her panting was soon replaced with the sounds of pleasure."
    m 4eublu "While this was taking place, Sayori and Yuri also stood to follow their respective partners."
    m 4rublu "Yuri eagerly pushed her hips backwards, grinding herself on the man's throbbing cock. Before the man took ahold of her shoulders and started roughly penetrating her."
    m 4wubld "Her moans were so loud!{w=0.3} Almost...animalistic, without a hint of restraint."
    m 4eublb "Sayori was compliant as well, her tight pussy was penetrated in quick order by the guy behind her."
    m 3wubld "As she was being taken from behind, she reached forward and grabbed a slice of the pizza, chewing on it with a lewd expression on her face."
    m 3hkblsdlb "But to be honest I'm not sure if the lewd sounds coming out of her were because of the sex, or the food!"
    m 3eubld "Eventually, the guy raised Sayori's right leg in the air for better access and forced himself balls-deep into her wet pussy with slow, heavy thrusts that brought lustful moans out of her."
    m 3rublu "Meanwhile the forth guy walked around the table and in front of the girls, slowly pleasuring himself to the sight of the three girls being ravaged."
    m 3gublu "As he was nearing his climax, he walked up to Sayori and came all over her pizza..."
    m 3wubld "He repeated this twice more and finally, Natsuki, Sayori and Yuri were all served a nice and delicious-looking, cum-glazed pizza..."
    m 4eublu "Without even finishing yet, the three guys pulled out of the girls, and helped them down sit down, though they seemed to struggle a little after the pounding they had received."
    m 4tublu "Exhausted from the dicking they had been given, all three girls leaned on the table, resting their heads in front of the cum-covered pizzas."
    m 1hublb "Ahaha...this was when the real fun was about to begin."
    m 1gublu "The guys each reached for the semen-coated pizzas and took a slice for each girl and began feeding them the improved food with their secret ingredient: love{w=0.5}{nw}"
    extend 1gublb "...juices. Ahaha~"
    m 1eublc "Though Natsuki seemed reluctant, she agreed to take a few bites. She chewed on them for a long, long time before swallowing."
    m 1tkbld "I couldn't blame her. The taste was probably awful, it was written all over her face."
    m 3eubld "But she complied, probably because she wanted to get it over with more than anything else."
    m 3wubld "Sayori on the other hand went all crazy for it, devouring anything that the guys put in her mouth - and would no matter what, always give them a smile and ask for more afterwards."
    m 3hublb "In between two bites I could even hear Sayori saying: 'What a weird dream! This feels so real!'"
    m 3hkblsdlb "Oh, poor Sayori...If only you knew...Ahaha~"
    m 3rublb "Yuri didn't show much interest in eating the food, but she did show a great interest in licking up all the cum."
    m 2tubla "Any time the guys would try to feed her the pizza she just leaned forward and cleaned the semen off of it with a lewd expression, refusing to eat the food..."
    m 2rublb "It was all incredibly crazy and surreal, but I loved every second of it!"
    m 5eubla "As for what happened after this? I think I'll leave that for another time~"
    m 5hubla "I hope you enjoyed my story, [player]~"
    return