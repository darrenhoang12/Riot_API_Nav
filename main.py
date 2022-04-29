import tkinter as tk
import tkinter.font as font
import RiotAPIBackend as RiotAPI
from PIL import ImageTk, Image


class RiotDirectoryApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("LOL and Valorant Navigation App for Desktops")
        self.geometry("985x720")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for page in (Homepage, LeagueLeaderboard, ProPlay, PersonalStats,
                     Guides, LeagueGuides, ValorantGuides, ValorantLeaderboard):
            page_name = page.__name__
            frame = page(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.switch_frame(Homepage)

    def switch_frame(self, page_name):
        frame = self.frames[page_name.__name__]
        frame.tkraise()

    @staticmethod
    def hovering(event):
        event.widget["background"] = "gray"

    @staticmethod
    def not_hovering(event):
        event.widget["background"] = "#2b2b2b"


class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")
        self.photo = Image.open("hp_wp.jpg")
        self.photo = self.photo.resize((825, 450))
        self.photo = ImageTk.PhotoImage(self.photo)

        self.nav_bar_font = font.Font(family="System", size=10)
        self.controller = controller

        label = tk.Label(self, text="WELCOME TO RIOT-NAV", height=2,
                         font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        label.grid(row=0, column=0, sticky="news", pady=10)

        # page_content frame holds all the page content such as navigation buttons and the data on the right
        page_content = tk.Frame(self, background="#2b2b2b")
        page_content.grid(row=1, column=0, sticky="w")

        self.create_nav_bar(page_content)
        self.create_nav_bar(page_content)

    def create_nav_bar(self, frame):
        # nav_bar frame holds the side navigation buttons
        nav_bar = tk.Frame(frame, background="#2b2b2b")
        nav_bar.grid(row=0, column=0, sticky="w")

        home = tk.Button(nav_bar, text="Home",
                         width=20, height=2, highlightthickness=0, bd=0,
                         font=self.nav_bar_font, bg="#2b2b2b", fg="white")
        league_lb = tk.Button(nav_bar, text="League of Legends",
                              width=20, height=2, highlightthickness=0, bd=0,
                              font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                              command=lambda: self.controller.switch_frame(LeagueLeaderboard))
        pro_play = tk.Button(nav_bar, text="Pro Matches",
                             width=20, height=2, highlightthickness=0, bd=0,
                             font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                             command=lambda: self.controller.switch_frame(ProPlay))
        personal_stats = tk.Button(nav_bar, text="Match History",
                                   width=20, height=2, highlightthickness=0, bd=0,
                                   font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                                   command=lambda: self.controller.switch_frame(PersonalStats))
        guides = tk.Button(nav_bar, text="Guides",
                           width=20, height=2, highlightthickness=0, bd=0,
                           font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                           command=lambda: self.controller.switch_frame(Guides))
        valorant_lb = tk.Button(nav_bar, text="Valorant",
                                width=20, height=2, highlightthickness=0, bd=0,
                                font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                                command=lambda: self.controller.switch_frame(ValorantLeaderboard))

        dir_widgets = [home, league_lb, pro_play, personal_stats, guides, valorant_lb]
        for idx in range(6):
            dir_widgets[idx].grid(row=0, column=idx)

        dir_widgets.remove(home)
        for widget in dir_widgets:
            widget.bind("<Enter>", self.controller.hovering)
            widget.bind("<Leave>", self.controller.not_hovering)

        main_content_frame = tk.Frame(frame, bg="#2b2b2b", width=800, height=500)
        main_content_frame.grid(row=1, column=0, sticky="n")

        img = tk.Label(main_content_frame, bg="#2b2b2b", image=self.photo)
        img.place(x=0, y=0, relwidth=1, relheight=1)

        created_by_label = tk.Label(self, text="Created by Darren Hoang, UCI, 2022",
                                    bg="#2b2b2b", fg="white", font=("Helvetica", 8))
        created_by_label.grid(row=7, column=0, sticky="sw")
        self.grid_rowconfigure(7, weight=1)


class LeagueLeaderboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")
        self.nav_bar_font = font.Font(family="System", size=10)
        self.controller = controller

        page_title = tk.Label(self, text="LEAGUE OF LEGENDS LEADERBOARD", height=2,
                              font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        page_title.grid(row=0, column=0, sticky="news", pady=10)

        page_content = tk.Frame(self, bg="#2b2b2b")
        page_content.grid(row=1, column=0, sticky="w")

        self.create_nav_bar(page_content)

    def create_nav_bar(self, frame):
        nav_bar = tk.Frame(frame, bg="#2b2b2b")
        nav_bar.grid(row=0, column=0, sticky="w")

        home = tk.Button(nav_bar, text="Home",
                         width=20, height=2, highlightthickness=0, bd=0,
                         font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                         command=lambda: self.controller.switch_frame(Homepage))

        league_lb = tk.Button(nav_bar, text="League of Legends",
                              width=20, height=2, highlightthickness=0, bd=0,
                              font=self.nav_bar_font, bg="#2b2b2b", fg="white")

        pro_play = tk.Button(nav_bar, text="Pro Matches",
                             width=20, height=2, highlightthickness=0, bd=0,
                             font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                             command=lambda: self.controller.switch_frame(ProPlay))

        personal_stats = tk.Button(nav_bar, text="Match History",
                                   width=20, height=2, highlightthickness=0, bd=0,
                                   font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                                   command=lambda: self.controller.switch_frame(PersonalStats))

        guides = tk.Button(nav_bar, text="Guides",
                           width=20, height=2, highlightthickness=0, bd=0,
                           font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                           command=lambda: self.controller.switch_frame(Guides))

        valorant_lb = tk.Button(nav_bar, text="Valorant",
                                width=20, height=2, highlightthickness=0, bd=0,
                                font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                                command=lambda: self.controller.switch_frame(ValorantLeaderboard))

        dir_widgets = [home, league_lb, pro_play, personal_stats, guides, valorant_lb]
        for idx in range(6):
            dir_widgets[idx].grid(row=0, column=idx)

        dir_widgets.remove(league_lb)
        for widget in dir_widgets:
            widget.bind("<Enter>", self.controller.hovering)
            widget.bind("<Leave>", self.controller.not_hovering)

        created_by_label = tk.Label(self, text="Created by Darren Hoang, UCI, 2022",
                                    bg="#2b2b2b", fg="white", font=("Helvetica", 8))
        created_by_label.grid(row=7, column=0, sticky="sw")
        self.grid_rowconfigure(7, weight=1)
        # LeagueLeaderboard.get_leaderboard_data()

    @staticmethod
    def get_leaderboard_data():
        league_leaderboard = RiotAPI.get_challenger_leaderboard()


class ProPlay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")
        self.nav_bar_font = font.Font(family="System", size=10)
        self.controller = controller

        page_title = tk.Label(self, text="PRO MATCHES", height=2,
                              font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        page_title.grid(row=0, column=0, sticky="news", pady=10)

        page_content = tk.Frame(self, bg="#2b2b2b")
        page_content.grid(row=1, column=0, sticky="w")

        self.create_nav_bar(page_content)

    def create_nav_bar(self, frame):
        nav_bar = tk.Frame(frame, bg="#2b2b2b")
        nav_bar.grid(row=0, column=0, sticky="w")

        home = tk.Button(nav_bar, text="Home",
                         width=20, height=2, highlightthickness=0, bd=0,
                         font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                         command=lambda: self.controller.switch_frame(Homepage))

        league_lb = tk.Button(nav_bar, text="League of Legends",
                              width=20, height=2, highlightthickness=0, bd=0,
                              font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                              command=lambda: self.controller.switch_frame(LeagueLeaderboard))

        pro_play = tk.Button(nav_bar, text="Pro Matches",
                             width=20, height=2, highlightthickness=0, bd=0,
                             font=self.nav_bar_font, bg="#2b2b2b", fg="white")

        personal_stats = tk.Button(nav_bar, text="Match History",
                                   width=20, height=2, highlightthickness=0, bd=0,
                                   font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                                   command=lambda: self.controller.switch_frame(PersonalStats))

        guides = tk.Button(nav_bar, text="Guides",
                           width=20, height=2, highlightthickness=0, bd=0,
                           font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                           command=lambda: self.controller.switch_frame(Guides))

        valorant_lb = tk.Button(nav_bar, text="Valorant",
                                width=20, height=2, highlightthickness=0, bd=0,
                                font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                                command=lambda: self.controller.switch_frame(ValorantLeaderboard))

        dir_widgets = [home, league_lb, pro_play, personal_stats, guides, valorant_lb]
        for idx in range(6):
            dir_widgets[idx].grid(row=0, column=idx)

        dir_widgets.remove(pro_play)
        for widget in dir_widgets:
            widget.bind("<Enter>", self.controller.hovering)
            widget.bind("<Leave>", self.controller.not_hovering)

        created_by_label = tk.Label(self, text="Created by Darren Hoang, UCI, 2022",
                                    bg="#2b2b2b", fg="white", font=("Helvetica", 8))
        created_by_label.grid(row=7, column=0, sticky="sw")
        self.grid_rowconfigure(7, weight=1)


class PersonalStats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")
        self.summoner_name = tk.StringVar()
        self.summoner_tagline = tk.StringVar()

        self.guides_bg = Image.open("guides_bg.jpg")
        self.guides_bg = self.guides_bg.resize((825, 450))
        self.guides_bg = ImageTk.PhotoImage(self.guides_bg)

        self.nav_bar_font = font.Font(family="System", size=10)
        self.controller = controller

        page_title = tk.Label(self, text="MATCH HISTORY", height=2,
                              font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        page_title.grid(row=0, column=0, sticky="news", pady=10)

        nav_bar = tk.Frame(self, bg="#2b2b2b")
        nav_bar.grid(row=1, column=0, sticky="w")

        main_content = tk.Frame(self, bg="#2b2b2b", width=985, height=500)
        main_content.grid(row=2, column=0, sticky="w")
        main_content.grid_propagate(False)

        self.create_nav_bar(nav_bar)
        self.input_summoner_name_info(main_content)

    def create_nav_bar(self, frame):
        nav_bar = tk.Frame(frame, bg="#2b2b2b")
        nav_bar.grid(row=0, column=0, sticky="w")

        home = tk.Button(nav_bar, text="Home",
                         width=20, height=2, highlightthickness=0, bd=0,
                         font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                         command=lambda: self.controller.switch_frame(Homepage))

        league_lb = tk.Button(nav_bar, text="League of Legends",
                              width=20, height=2, highlightthickness=0, bd=0,
                              font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                              command=lambda: self.controller.switch_frame(LeagueLeaderboard))

        pro_play = tk.Button(nav_bar, text="Pro Matches",
                             width=20, height=2, highlightthickness=0, bd=0,
                             font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                             command=lambda: self.controller.switch_frame(ProPlay))

        personal_stats = tk.Button(nav_bar, text="Match History",
                                   width=20, height=2, highlightthickness=0, bd=0,
                                   font=self.nav_bar_font, bg="#2b2b2b", fg="white")

        guides = tk.Button(nav_bar, text="Guides",
                           width=20, height=2, highlightthickness=0, bd=0,
                           font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                           command=lambda: self.controller.switch_frame(Guides))

        valorant_lb = tk.Button(nav_bar, text="Valorant",
                                width=20, height=2, highlightthickness=0, bd=0,
                                font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                                command=lambda: self.controller.switch_frame(ValorantLeaderboard))

        dir_widgets = [home, league_lb, pro_play, personal_stats, guides, valorant_lb]
        for idx in range(6):
            dir_widgets[idx].grid(row=0, column=idx)

        dir_widgets.remove(personal_stats)
        for widget in dir_widgets:
            widget.bind("<Enter>", self.controller.hovering)
            widget.bind("<Leave>", self.controller.not_hovering)

        created_by_label = tk.Label(self, text="Created by Darren Hoang, UCI, 2022",
                                    bg="#2b2b2b", fg="white", font=("Helvetica", 8))
        created_by_label.grid(row=7, column=0, sticky="sw")
        self.grid_rowconfigure(7, weight=1)

    def input_summoner_name_info(self, frame):
        background_label = tk.Label(frame, image=self.guides_bg, bg="#2b2b2b")
        entry_summoner_name = tk.Entry(frame, textvariable=self.summoner_name, width=25)
        hash_label = tk.Label(frame, text="#", font=font.Font(weight="bold"), bg="#2b2b2b", fg="white")
        entry_summoner_tagline = tk.Entry(frame, textvariable=self.summoner_tagline, width=15)
        search_button = tk.Button(frame, text="SEARCH", font=self.nav_bar_font, bg="white",
                                  command=lambda: self.create_stats(self.summoner_name.get(),
                                                                    self.summoner_tagline.get(), frame))

        background_label.place(x=200, y=85, relheight=1, relwidth=1)
        hash_label.place(x=274, y=29)

        entry_summoner_name.place(x=62, y=30)
        entry_summoner_name.insert(0, "Summoner name...")
        entry_summoner_name.config(fg="grey", font=font.Font(family="System"))
        entry_summoner_name.bind("<FocusIn>", lambda event: PersonalStats.on_entry_click(event, "Summoner name..."))
        entry_summoner_name.bind("<FocusOut>", lambda event: PersonalStats.on_focus_out(event, "Summoner name..."))

        entry_summoner_tagline.place(x=290, y=30)
        entry_summoner_tagline.insert(0, "Tagline...")
        entry_summoner_tagline.config(fg="grey", font=font.Font(family="System"))
        entry_summoner_tagline.bind("<FocusIn>", lambda event: PersonalStats.on_entry_click(event, "Tagline..."))
        entry_summoner_tagline.bind("<FocusOut>", lambda event: PersonalStats.on_focus_out(event, "Tagline..."))

        self.controller.bind("<Return>",
                             lambda event: PersonalStats.create_stats(self.summoner_name.get(),
                                                                      self.summoner_tagline.get(), frame))
        search_button.place(x=420, y=27)

    @staticmethod
    def create_stats(summoner_name, summoner_tagline, frame):
        match_history = RiotAPI.get_personal_statistics(summoner_name, summoner_tagline)
        champions_played = []
        kills_match = []
        deaths_match = []
        assists_match = []
        wins = []

        for match in match_history:
            champions_played.append(match["championName"])
            kills_match.append(match["kills"])
            deaths_match.append(match["deaths"])
            assists_match.append(match["assists"])
            wins.append(match["win"])
        print(champions_played)
        print(kills_match)
        print(deaths_match)
        print(assists_match)
        print(wins)

        new_f = tk.Frame(frame)
        new_f.grid(row=2, column=0)

        i = 90
        for champion in champions_played:
            tk.Button(frame, text=champion, width=90, height=4,
                      font=font.Font(family="System", size=10)).place(x=62, y=i)
            i += 80

    @staticmethod
    def on_entry_click(event, message):
        if event.widget.get() == message:
            event.widget.delete(0, "end")
            event.widget.insert(0, "")
            event.widget.config(fg="black", font=font.Font(family="System"))

    @staticmethod
    def on_focus_out(event, message):
        if event.widget.get() == "":
            event.widget.insert(0, message)
            event.widget.config(fg="gray", font=font.Font(family="System"))


class Guides(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")

        self.guides_bg = Image.open("guides_bg.jpg")
        self.guides_bg = self.guides_bg.resize((825, 450))
        self.guides_bg = ImageTk.PhotoImage(self.guides_bg)

        self.league_logo = Image.open("league_logo.jpeg")
        self.league_logo = self.league_logo.resize((150, 150))
        self.league_logo = ImageTk.PhotoImage(self.league_logo)

        self.valorant_logo = Image.open("valorant_logo.png")
        self.valorant_logo = self.valorant_logo.resize((150, 150))
        self.valorant_logo = ImageTk.PhotoImage(self.valorant_logo)

        self.nav_bar_font = font.Font(family="System", size=10)
        self.controller = controller

        page_title = tk.Label(self, text="GUIDES", height=2,
                              font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        page_title.grid(row=0, column=0, sticky="news", pady=10)

        # must add in order to add things to the right of the side navigation.
        nav_bar = tk.Frame(self, bg="#2b2b2b")
        nav_bar.grid(row=1, column=0, sticky="w")

        main_content = tk.Frame(self, bg="#2b2b2b", width=985, height=500)
        main_content.grid(row=2, column=0, sticky="w")
        main_content.grid_propagate(False)

        self.create_nav(nav_bar)
        self.create_main_content(main_content)

    def create_nav(self, frame):
        nav_bar = tk.Frame(frame, bg="#2b2b2b")
        nav_bar.grid(row=0, column=0, sticky="w")

        home = tk.Button(nav_bar, text="Home",
                         width=20, height=2, highlightthickness=0, bd=0,
                         font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                         command=lambda: self.controller.switch_frame(Homepage))

        league_lb = tk.Button(nav_bar, text="League of Legends",
                              width=20, height=2, highlightthickness=0, bd=0,
                              font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                              command=lambda: self.controller.switch_frame(LeagueLeaderboard))

        pro_play = tk.Button(nav_bar, text="Pro Matches",
                             width=20, height=2, highlightthickness=0, bd=0,
                             font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                             command=lambda: self.controller.switch_frame(ProPlay))

        personal_stats = tk.Button(nav_bar, text="Match History",
                                   width=20, height=2, highlightthickness=0, bd=0,
                                   font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                                   command=lambda: self.controller.switch_frame(PersonalStats))

        guides = tk.Button(nav_bar, text="Guides",
                           width=20, height=2, highlightthickness=0, bd=0,
                           font=self.nav_bar_font, bg="#2b2b2b", fg="white")

        valorant_lb = tk.Button(nav_bar, text="Valorant",
                                width=20, height=2, highlightthickness=0, bd=0,
                                font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                                command=lambda: self.controller.switch_frame(ValorantLeaderboard))

        dir_widgets = [home, league_lb, pro_play, personal_stats, guides, valorant_lb]
        for idx in range(6):
            dir_widgets[idx].grid(row=0, column=idx)

        dir_widgets.remove(guides)
        for widget in dir_widgets:
            widget.bind("<Enter>", self.controller.hovering)
            widget.bind("<Leave>", self.controller.not_hovering)

    def create_main_content(self, frame):
        background_label = tk.Label(frame, image=self.guides_bg, bg="#2b2b2b")

        league_guides = tk.Button(frame, text="League Guides",
                                  height=2, highlightthickness=0, bd=0,
                                  font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                                  command=lambda: self.controller.switch_frame(LeagueGuides))
        valorant_guides = tk.Button(frame, text="Valorant Guides",
                                    height=2, highlightthickness=0, bd=0,
                                    font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                                    command=lambda: self.controller.switch_frame(ValorantGuides))

        lol_logo = tk.Button(frame, image=self.league_logo, bg="#2b2b2b",
                             command=lambda: self.controller.switch_frame(LeagueGuides))
        val_logo = tk.Button(frame, image=self.valorant_logo, bg="#2b2b2b",
                             command=lambda: self.controller.switch_frame(ValorantGuides))

        background_label.place(x=200, y=85, relheight=1, relwidth=1)
        lol_logo.grid(row=0, column=0, padx=200, pady=(100, 15))
        league_guides.grid(row=1, column=0)
        val_logo.grid(row=0, column=1, padx=50, pady=(100, 15))
        valorant_guides.grid(row=1, column=1)

        for widget in (league_guides, valorant_guides):
            widget.bind("<Enter>", self.controller.hovering)
            widget.bind("<Leave>", self.controller.not_hovering)

        created_by_label = tk.Label(self, text="Created by Darren Hoang, UCI, 2022",
                                    bg="#2b2b2b", fg="white", font=("Helvetica", 8))
        created_by_label.grid(row=7, column=0, sticky="sw")
        self.grid_rowconfigure(7, weight=1)


class LeagueGuides(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")
        self.guide_nav_bar_font = font.Font(family="System", size=18)
        self.controller = controller

        page_title = tk.Label(self, text="LEAGUE OF LEGENDS GUIDES", height=2,
                              font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        page_title.grid(row=0, column=0, sticky="news", pady=10)
        break_line = tk.Label(self, text="", bg="white", height=0)
        break_line.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)

        self.create_guide_nav_buttons()

    def create_guide_nav_buttons(self):
        guide_nav_bar = tk.Frame(self, bg="#2b2b2b")
        guide_nav_bar.grid(row=2, column=0, sticky="news")

        guides_home = tk.Button(guide_nav_bar, text="To Guides Homepage",
                                width=30, highlightthickness=0, bd=0,
                                font=self.guide_nav_bar_font, bg="#2b2b2b", fg="white",
                                command=lambda: self.controller.switch_frame(Guides))
        league_guides = tk.Button(guide_nav_bar, text="-> League Guides",
                                  width=30, highlightthickness=0, bd=0,
                                  font=self.guide_nav_bar_font, bg="#2b2b2b", fg="white")
        valorant_guides = tk.Button(guide_nav_bar, text="To Valorant Guides",
                                    width=30, highlightthickness=0, bd=0,
                                    font=self.guide_nav_bar_font, bg="#2b2b2b", fg="white",
                                    command=lambda: self.controller.switch_frame(ValorantGuides))

        guide_nav_widgets = [guides_home, league_guides, valorant_guides]
        for idx in range(len(guide_nav_widgets)):
            guide_nav_widgets[idx].grid(row=0, column=idx)
        guide_nav_bar.grid_columnconfigure((0, 1, 2), weight=1, uniform="column")

        for button in guide_nav_widgets:
            button.bind("<Enter>", self.controller.hovering)
            button.bind("<Leave>", self.controller.not_hovering)


class ValorantGuides(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")
        self.guide_nav_bar_font = font.Font(family="System", size=18)
        self.controller = controller

        page_title = tk.Label(self, text="VALORANT GUIDES", height=2,
                              font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        page_title.grid(row=0, column=0, sticky="news", pady=10)
        break_line = tk.Label(self, text="", bg="white", height=0)
        break_line.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)

        self.create_guide_nav_buttons()

    def create_guide_nav_buttons(self):
        guide_nav_bar = tk.Frame(self, bg="#2b2b2b")
        guide_nav_bar.grid(row=2, column=0, sticky="news")

        guides_home = tk.Button(guide_nav_bar, text="To Guides Homepage",
                                width=30, highlightthickness=0, bd=0,
                                font=self.guide_nav_bar_font, bg="#2b2b2b", fg="white",
                                command=lambda: self.controller.switch_frame(Guides))
        league_guides = tk.Button(guide_nav_bar, text="To League Guides",
                                  width=30, highlightthickness=0, bd=0,
                                  font=self.guide_nav_bar_font, bg="#2b2b2b", fg="white",
                                  command=lambda: self.controller.switch_frame(LeagueGuides))
        valorant_guides = tk.Button(guide_nav_bar, text="-> Valorant Guides",
                                    width=30, highlightthickness=0, bd=0,
                                    font=self.guide_nav_bar_font, bg="#2b2b2b", fg="white")

        guide_nav_widgets = [guides_home, league_guides, valorant_guides]
        for idx in range(len(guide_nav_widgets)):
            guide_nav_widgets[idx].grid(row=0, column=idx)
        guide_nav_bar.grid_columnconfigure((0, 1, 2), weight=1, uniform="column")

        for button in guide_nav_widgets:
            button.bind("<Enter>", self.controller.hovering)
            button.bind("<Leave>", self.controller.not_hovering)


class ValorantLeaderboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")
        self.nav_bar_font = font.Font(family="System", size=10)
        self.controller = controller

        page_title = tk.Label(self, text="RADIANT LEADERBOARD", height=2,
                              font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        page_title.grid(row=0, column=0, sticky="news", pady=10)

        page_content = tk.Frame(self, bg="#2b2b2b")
        page_content.grid(row=1, column=0, sticky="w")

        self.create_nav_bar(page_content)

    def create_nav_bar(self, frame):
        nav_bar = tk.Frame(frame, bg="#2b2b2b")
        nav_bar.grid(row=0, column=0, sticky="w")

        home = tk.Button(nav_bar, text="Home",
                         width=20, height=2, highlightthickness=0, bd=0,
                         font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                         command=lambda: self.controller.switch_frame(Homepage))

        league_lb = tk.Button(nav_bar, text="League of Legends",
                              width=20, height=2, highlightthickness=0, bd=0,
                              font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                              command=lambda: self.controller.switch_frame(LeagueLeaderboard))

        pro_play = tk.Button(nav_bar, text="Pro Matches",
                             width=20, height=2, highlightthickness=0, bd=0,
                             font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                             command=lambda: self.controller.switch_frame(ProPlay))

        personal_stats = tk.Button(nav_bar, text="Match History",
                                   width=20, height=2, highlightthickness=0, bd=0,
                                   font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                                   command=lambda: self.controller.switch_frame(PersonalStats))

        guides = tk.Button(nav_bar, text="Guides",
                           width=20, height=2, highlightthickness=0, bd=0,
                           font=self.nav_bar_font, bg="#2b2b2b", fg="white",
                           command=lambda: self.controller.switch_frame(Guides))

        valorant_lb = tk.Button(nav_bar, text="Valorant",
                                width=20, height=2, highlightthickness=0, bd=0,
                                font=self.nav_bar_font, bg="#2b2b2b", fg="white")

        dir_widgets = [home, league_lb, pro_play, personal_stats, guides, valorant_lb]
        for idx in range(6):
            dir_widgets[idx].grid(row=0, column=idx)

        dir_widgets.remove(valorant_lb)
        for widget in dir_widgets:
            widget.bind("<Enter>", self.controller.hovering)
            widget.bind("<Leave>", self.controller.not_hovering)

        created_by_label = tk.Label(self, text="Created by Darren Hoang, UCI, 2022",
                                    bg="#2b2b2b", fg="white", font=("Helvetica", 8))
        created_by_label.grid(row=7, column=0, sticky="sw")
        self.grid_rowconfigure(7, weight=1)


if __name__ == "__main__":
    app = RiotDirectoryApp()
    for i in RiotAPI.get_personal_statistics("ChuuOnDeezNutz", "loona"):
        print(i)
    # RiotAPI.get_radiant_valorant_leaderboard()
    app.mainloop()
