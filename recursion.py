file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"


def finder(file_system, target):

    for txt in file_system:
        if txt == target:
            print("Horray")
        elif isinstance(txt, list):
            response = finder(txt, target)
            if response == "Horray":
                print(response)
                  

finder(file_system, target)