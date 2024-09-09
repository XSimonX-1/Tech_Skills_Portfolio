TD_FILTER = [
    ("", [], [], 0),
    ("soup", [], [], 0),
    ("", ["Hard"], [], 0),
    ("", [], ["Expensive"], 0),
    ("", [], [], 12),
    ("", ["Medium"], ["Medium"], 0),
    ("hungarian", [], [], 5),
    ("", ["Easy"], [], 180),
    ("pasta", ["Easy", "Medium"], ["Cheap"], 50),
    ("", ["Easy", "Medium", "Hard"], ["Cheap", "Medium", "Expensive"], 0)
]

TD_RECIPE_NR = [15, 10, 8, 6, 4]

TD_INGREDIENT = [
    ["cheese"],
    ["tomato", "salt"],
    ["beef", "onion", "coriander"]
]

TD_SEARCH = [
    ("pancake", True),
    ("Zucchini", False)
]

TD_RATING = [
    ("xxx@gmail.com", "xxxx", "Carrot Cake"),
    ("xxx@gmail.com", "xxxx", "Classic Mojito")
]

TD_COMMENT = [
    ("xxx@gmail.com", "xxxx", "Carrot Cake", "davido", "El fogom készíteni"),
    ("xxx@gmail.com", "xxxx", "Carrot Cake", "", "Nincs megadva név"),
    ("xxx@gmail.com", "xxxx", "Classic Mojito",
     "Ez egy 255 karakternél hosszabb szöveg                                                                                                                                                                                                                itt a vége",
     "Szeretném megfőzni")
]

TD_FOLLOW_AUTHOR = [
    ("xxx@gmail.com", "xxxx", "Petra", "xxx@gmail.com"),
    ("xxx@gmail.com", "xxxx", "Jakab", "xxx@freemail.hu"),
]
