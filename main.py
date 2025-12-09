from pyscript import document, display
#club information dictionary
club_info = {

    "socsci": {
        "name": "Social Science Club",
        "description": "A club for Politics nerds.",
        "meeting_time": "Tuesday and Wednesday, 3:00 PM - 4:00 PM",
        "Venue": "Room 409",
        "moderator": "Roberto Lim Jr.",
        "members": 22
    },

    "cac": {
        "name": "Communications Arts Club",
        "description": "OBMC's fanfic writers",
        "meeting_time": "Wednesday and Friday, 3:00 PM - 4:00 PM",
        "Venue": "Room 406",
        "moderator": "Yannis Fernandez",
        "members": 19
    },

    "mat": {
        "name": "Math Club",
        "description": "A club for math wizards",
        "meeting_time": "Monday, 2:30 PM - 3:00 PM",
        "Venue": "Room 408",
        "moderator": "Nicole Gabuya",
        "members": 20
    },

    "b": {
        "name": "Marching Band",
        "description": "A club for music lovers",
        "meeting_time": " Tuesday and Wednesday, 3:00 PM - 4:30 PM",
        "Venue": "Band Room",
        "moderator": "Emilio Alumno",
        "members": 30
    },

    "dc": {
        "name": "Dance Club",
        "description": "A club for dancers.",
        "meeting_time": "Tuesday, 3:00 PM - 5:00 PM",
        "Venue": "Teatro Preciosa",
        "moderator": "Alfred Cases",
        "members": 32
    },
    "bbc": {
        "name": "Basketball Varsity",
        "description": "The Future Fairview D-League Champs",
        "meeting_time": "Monday, 3:00 PM - 4:00 PM",
        "Venue": "Quadrangle",
        "moderator": "Adrian Ruiz",
        "members": 20
    }
}
#function to display club information
def show_club_info(e):
    selected_club = document.getElementById("Clubs").value
    info = club_info.get(selected_club)
#summary
    if info:
        summary = f"""
<b>Club Name:</b> {info["name"]}<br>
<b>Description:</b> {info["description"]}<br>
<b>Meeting Time:</b> {info["meeting_time"]}<br>
<b>Venue:</b> {info["Venue"]}<br>
<b>Moderator:</b> {info["moderator"]}<br>
<b>Number of Members:</b> {info["members"]}
        """
        document.getElementById("output").innerHTML = summary
    else:
        document.getElementById("output").innerHTML = "Club information not found."
