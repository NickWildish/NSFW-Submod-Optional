init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_dev_othergirls_fix",
            category=['NSFW DEV'],
            prompt="UNLOCK OTHERGIRLS STORIES",
            pool=True,
            unlocked=True
        )
    )

label nsfw_dev_othergirls_fix:
    m 1eua "Checking state of 'othergirls' stories..."
    if mas_isPoolEVL("nsfw_erotic_story_natsuki_deepthroat") or not mas_isUnlockedEVL("nsfw_erotic_story_natsuki_deepthroat"):
        m 1eua "Natsuki story error detected. Attempting fix..."
        $ mas_setEVLPropValues("nsfw_erotic_story_natsuki_deepthroat", pool=False, unlocked=True)
        m 1eua "Natsuki story fix successful."
    if mas_isPoolEVL("nsfw_erotic_story_sayori_ballscleaning") or not mas_isUnlockedEVL("nsfw_erotic_story_sayori_ballscleaning"):
        m 1eua "Sayori story error detected. Attempting fix..."
        $ mas_setEVLPropValues("nsfw_erotic_story_sayori_ballscleaning", pool=False, unlocked=True)
        m 1eua "Sayori story fix successful."
    if mas_isPoolEVL("nsfw_erotic_story_yuri_titjob") or not mas_isUnlockedEVL("nsfw_erotic_story_yuri_titjob"):
        m 1eua "Yuri story error detected. Attempting fix..."
        $ mas_setEVLPropValues("nsfw_erotic_story_yuri_titjob", pool=False, unlocked=True)
        m 1eua "Yuri story fix successful."
    if mas_isPoolEVL("nsfw_erotic_story_club_pizza_party") or not mas_isUnlockedEVL("nsfw_erotic_story_club_pizza_party"):
        m 1eua "Pizza party story error detected. Attempting fix..."
        $ mas_setEVLPropValues("nsfw_erotic_story_club_pizza_party", pool=False, unlocked=True)
        m 1eua "Pizza party story fix successful."
    m 1eua "Fix complete."