import tkinter as tk
import tkinter.font as font
import RiotAPIBackend as RiotAPI
from PIL import ImageTk, Image


class RiotDirectoryApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_attributes("-transparentcolor", "yellow")
        self.title("LOL and Valorant Navigation App for Desktops")
        self.geometry("1200x650")

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


class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")
        self.photo = Image.open("hp_wp.jpg")
        self.photo = self.photo.resize((825, 450))
        self.photo = ImageTk.PhotoImage(self.photo)

        self.side_nav_font = font.Font(family="System", size=18)
        self.controller = controller

        label = tk.Label(self, text="WELCOME TO RIOT-NAV", height=2,
                         font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        label.grid(row=0, column=0, sticky="news", pady=10)
        break_line = tk.Label(self, text="", bg="white", height=0)
        break_line.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)

        # page_content frame holds all the page content such as navigation buttons and the data on the right
        page_content = tk.Frame(self, background="#2b2b2b")
        page_content.grid(row=2, column=0, sticky="w")
        self.grid_rowconfigure(2, weight=1)

        self.create_side_nav(page_content, controller)

    def create_side_nav(self, frame, controller):
        # side_nav frame holds the side navigation buttons
        side_nav = tk.Frame(frame, background="#2b2b2b")
        side_nav.grid(row=1, column=0, sticky="w")

        home = tk.Button(side_nav, text="-> Home",
                         width=20, height=2, highlightthickness=0, bd=0,
                         font=self.side_nav_font, bg="#2b2b2b", fg="white")
        league_lb = tk.Button(side_nav, text="League Leaderboard",
                              width=20, height=2, highlightthickness=0, bd=0,
                              font=self.side_nav_font, bg="#2b2b2b", fg="white",
                              command=lambda: controller.switch_frame(LeagueLeaderboard))
        pro_play = tk.Button(side_nav, text="Pro Matches",
                             width=20, height=2, highlightthickness=0, bd=0,
                             font=self.side_nav_font, bg="#2b2b2b", fg="white",
                             command=lambda: controller.switch_frame(ProPlay))
        personal_stats = tk.Button(side_nav, text="League Personal Stats",
                                   width=20, height=2, highlightthickness=0, bd=0,
                                   font=self.side_nav_font, bg="#2b2b2b", fg="white",
                                   command=lambda: controller.switch_frame(PersonalStats))
        guides = tk.Button(side_nav, text="Guides",
                           width=20, height=2, highlightthickness=0, bd=0,
                           font=self.side_nav_font, bg="#2b2b2b", fg="white",
                           command=lambda: controller.switch_frame(Guides))
        valorant_lb = tk.Button(side_nav, text="Valorant Leaderboard",
                                width=20, height=2, highlightthickness=0, bd=0,
                                font=self.side_nav_font, bg="#2b2b2b", fg="white",
                                command=lambda: controller.switch_frame(ValorantLeaderboard))

        dir_widgets = [home, league_lb, pro_play, personal_stats, guides, valorant_lb]
        for idx in range(6):
            dir_widgets[idx].grid(row=idx, column=0)

        def hovering(e):
            e.widget["background"] = "gray"

        def not_hovering(e):
            e.widget["background"] = "#2b2b2b"

        dir_widgets.remove(home)
        for widget in dir_widgets:
            widget.bind("<Enter>", hovering)
            widget.bind("<Leave>", not_hovering)

        main_content_frame = tk.Frame(frame, bg="#2b2b2b")
        main_content_frame.grid(row=1, column=1, padx=5)

        img = tk.Label(main_content_frame, bg="#2b2b2b", image=self.photo)
        img.grid(row=0, column=0, padx=5)

        created_by_label = tk.Label(self, text="Created by Darren Hoang, UCI, 2022",
                                    bg="#2b2b2b", fg="white", font=("Helvetica", 8))
        created_by_label.grid(row=7, column=0, sticky="sw")
        self.grid_rowconfigure(7, weight=1)


class LeagueLeaderboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")
        self.side_nav_font = font.Font(family="System", size=18)
        self.controller = controller

        title_frame = tk.Frame(self, bg="#2b2b2b")
        title_frame.grid(row=0, column=0, sticky="n", pady=10)

        page_title = tk.Label(self, text="LEAGUE OF LEGENDS LEADERBOARD", height=2,
                              font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        page_title.grid(row=0, column=0, sticky="news", pady=10)
        break_line = tk.Label(self, text="", bg="white", height=0)
        break_line.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)

        page_content = tk.Frame(self, bg="#2b2b2b")
        page_content.grid(row=2, column=0, sticky="w")
        self.grid_rowconfigure(2, weight=1)

        self.create_side_nav(page_content, controller)

    def create_side_nav(self, frame, controller):
        side_nav = tk.Frame(frame, bg="#2b2b2b")
        side_nav.grid(row=2, column=0, sticky="w")

        home = tk.Button(side_nav, text="Home",
                         width=20, height=2, highlightthickness=0, bd=0,
                         font=self.side_nav_font, bg="#2b2b2b", fg="white",
                         command=lambda: controller.switch_frame(Homepage))

        league_lb = tk.Button(side_nav, text="-> League Leaderboard",
                              width=20, height=2, highlightthickness=0, bd=0,
                              font=self.side_nav_font, bg="#2b2b2b", fg="white")

        pro_play = tk.Button(side_nav, text="Pro Matches",
                             width=20, height=2, highlightthickness=0, bd=0,
                             font=self.side_nav_font, bg="#2b2b2b", fg="white",
                             command=lambda: controller.switch_frame(ProPlay))

        personal_stats = tk.Button(side_nav, text="League Personal Stats",
                                   width=20, height=2, highlightthickness=0, bd=0,
                                   font=self.side_nav_font, bg="#2b2b2b", fg="white",
                                   command=lambda: controller.switch_frame(PersonalStats))

        guides = tk.Button(side_nav, text="Guides",
                           width=20, height=2, highlightthickness=0, bd=0,
                           font=self.side_nav_font, bg="#2b2b2b", fg="white",
                           command=lambda: controller.switch_frame(Guides))

        valorant_lb = tk.Button(side_nav, text="Valorant Leaderboard",
                                width=20, height=2, highlightthickness=0, bd=0,
                                font=self.side_nav_font, bg="#2b2b2b", fg="white",
                                command=lambda: controller.switch_frame(ValorantLeaderboard))

        dir_widgets = [home, league_lb, pro_play, personal_stats, guides, valorant_lb]
        for idx in range(6):
            dir_widgets[idx].grid(row=idx, column=0)

        def hovering(e):
            e.widget["background"] = "gray"

        def not_hovering(e):
            e.widget["background"] = "#2b2b2b"

        dir_widgets.remove(league_lb)
        for widget in dir_widgets:
            widget.bind("<Enter>", hovering)
            widget.bind("<Leave>", not_hovering)

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
        self.side_nav_font = font.Font(family="System", size=18)
        self.controller = controller

        page_title = tk.Label(self, text="PRO MATCHES", height=2,
                              font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        page_title.grid(row=0, column=0, sticky="news", pady=10)
        break_line = tk.Label(self, text="", bg="white", height=0)
        break_line.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)

        page_content = tk.Frame(self, bg="#2b2b2b")
        page_content.grid(row=2, column=0, sticky="w")
        self.grid_rowconfigure(2, weight=1)

        self.create_side_nav(page_content, controller)

    def create_side_nav(self, frame, controller):
        side_nav = tk.Frame(frame, bg="#2b2b2b")
        side_nav.grid(row=2, column=0, sticky="w")

        home = tk.Button(side_nav, text="Home",
                         width=20, height=2, highlightthickness=0, bd=0,
                         font=self.side_nav_font, bg="#2b2b2b", fg="white",
                         command=lambda: controller.switch_frame(Homepage))

        league_lb = tk.Button(side_nav, text="League Leaderboard",
                              width=20, height=2, highlightthickness=0, bd=0,
                              font=self.side_nav_font, bg="#2b2b2b", fg="white",
                              command=lambda: controller.switch_frame(LeagueLeaderboard))

        pro_play = tk.Button(side_nav, text="-> Pro Matches",
                             width=20, height=2, highlightthickness=0, bd=0,
                             font=self.side_nav_font, bg="#2b2b2b", fg="white")

        personal_stats = tk.Button(side_nav, text="League Personal Stats",
                                   width=20, height=2, highlightthickness=0, bd=0,
                                   font=self.side_nav_font, bg="#2b2b2b", fg="white",
                                   command=lambda: controller.switch_frame(PersonalStats))

        guides = tk.Button(side_nav, text="Guides",
                           width=20, height=2,  highlightthickness=0, bd=0,
                           font=self.side_nav_font, bg="#2b2b2b", fg="white",
                           command=lambda: controller.switch_frame(Guides))

        valorant_lb = tk.Button(side_nav, text="Valorant Leaderboard",
                                width=20, height=2, highlightthickness=0, bd=0,
                                font=self.side_nav_font, bg="#2b2b2b", fg="white",
                                command=lambda: controller.switch_frame(ValorantLeaderboard))

        dir_widgets = [home, league_lb, pro_play, personal_stats, guides, valorant_lb]
        for idx in range(6):
            dir_widgets[idx].grid(row=idx, column=0)

        def hovering(e):
            e.widget["background"] = "gray"

        def not_hovering(e):
            e.widget["background"] = "#2b2b2b"

        dir_widgets.remove(pro_play)
        for widget in dir_widgets:
            widget.bind("<Enter>", hovering)
            widget.bind("<Leave>", not_hovering)

        created_by_label = tk.Label(self, text="Created by Darren Hoang, UCI, 2022",
                                    bg="#2b2b2b", fg="white", font=("Helvetica", 8))
        created_by_label.grid(row=7, column=0, sticky="sw")
        self.grid_rowconfigure(7, weight=1)


class PersonalStats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")
        self.side_nav_font = font.Font(family="System", size=18)
        self.controller = controller

        page_title = tk.Label(self, text="MATCH HISTORY", height=2,
                              font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        page_title.grid(row=0, column=0, sticky="news", pady=10)
        break_line = tk.Label(self, text="", bg="white", height=0)
        break_line.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)

        page_content = tk.Frame(self, bg="#2b2b2b")
        page_content.grid(row=2, column=0, sticky="w")
        self.grid_rowconfigure(2, weight=1)

        self.create_side_nav(page_content, controller)

    def create_side_nav(self, frame, controller):
        side_nav = tk.Frame(frame, bg="#2b2b2b")
        side_nav.grid(row=0, column=0, sticky="w")

        home = tk.Button(side_nav, text="Home",
                         width=20, height=2, highlightthickness=0, bd=0,
                         font=self.side_nav_font, bg="#2b2b2b", fg="white",
                         command=lambda: controller.switch_frame(Homepage))

        league_lb = tk.Button(side_nav, text="League Leaderboard",
                              width=20, height=2, highlightthickness=0, bd=0,
                              font=self.side_nav_font, bg="#2b2b2b", fg="white",
                              command=lambda: controller.switch_frame(LeagueLeaderboard))

        pro_play = tk.Button(side_nav, text="Pro Matches",
                             width=20, height=2, highlightthickness=0, bd=0,
                             font=self.side_nav_font, bg="#2b2b2b", fg="white",
                             command=lambda: controller.switch_frame(ProPlay))

        personal_stats = tk.Button(side_nav, text="-> League Personal Stats",
                                   width=20, height=2, highlightthickness=0, bd=0,
                                   font=self.side_nav_font, bg="#2b2b2b", fg="white")

        guides = tk.Button(side_nav, text="Guides",
                           width=20, height=2, highlightthickness=0, bd=0,
                           font=self.side_nav_font, bg="#2b2b2b", fg="white",
                           command=lambda: controller.switch_frame(Guides))

        valorant_lb = tk.Button(side_nav, text="Valorant Leaderboard",
                                width=20, height=2, highlightthickness=0, bd=0,
                                font=self.side_nav_font, bg="#2b2b2b", fg="white",
                                command=lambda: controller.switch_frame(ValorantLeaderboard))

        dir_widgets = [home, league_lb, pro_play, personal_stats, guides, valorant_lb]
        for idx in range(6):
            dir_widgets[idx].grid(row=idx, column=0)

        def hovering(e):
            e.widget["background"] = "gray"

        def not_hovering(e):
            e.widget["background"] = "#2b2b2b"

        dir_widgets.remove(personal_stats)
        for widget in dir_widgets:
            widget.bind("<Enter>", hovering)
            widget.bind("<Leave>", not_hovering)

        created_by_label = tk.Label(self, text="Created by Darren Hoang, UCI, 2022",
                                    bg="#2b2b2b", fg="white", font=("Helvetica", 8))
        created_by_label.grid(row=7, column=0, sticky="sw")
        self.grid_rowconfigure(7, weight=1)


class Guides(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")

        self.guides_bg = Image.open("guides_bg.jpg")
        self.guides_bg = self.guides_bg.resize((825, 470))
        self.guides_bg = ImageTk.PhotoImage(self.guides_bg)

        self.league_logo = Image.open("league_logo.jpeg")
        self.league_logo = self.league_logo.resize((150,150))
        self.league_logo = ImageTk.PhotoImage(self.league_logo)

        self.valorant_logo = Image.open("valorant_logo.png")
        self.valorant_logo = self.valorant_logo.resize((150, 150))
        self.valorant_logo = ImageTk.PhotoImage(self.valorant_logo)

        self.side_nav_font = font.Font(family="System", size=18)
        self.controller = controller

        page_title = tk.Label(self, text="GUIDES", height=2,
                              font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        page_title.grid(row=0, column=0, sticky="news", pady=10)
        break_line = tk.Label(self, text="", bg="white", height=0)
        break_line.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)

        # must add in order to add things to the right of the side navigation.
        page_content = tk.Frame(self, bg="#2b2b2b")
        page_content.grid(row=2, column=0, sticky="w")
        self.grid_rowconfigure(2, weight=1)

        self.create_side_nav_and_guide_buttons(page_content, controller)

    def create_side_nav_and_guide_buttons(self, frame, controller):
        side_nav = tk.Frame(frame, bg="#2b2b2b")
        side_nav.grid(row=0, column=0, sticky="w")

        home = tk.Button(side_nav, text="Home",
                         width=20, height=2, highlightthickness=0, bd=0,
                         font=self.side_nav_font, bg="#2b2b2b", fg="white",
                         command=lambda: controller.switch_frame(Homepage))

        league_lb = tk.Button(side_nav, text="League Leaderboard",
                              width=20, height=2, highlightthickness=0, bd=0,
                              font=self.side_nav_font, bg="#2b2b2b", fg="white",
                              command=lambda: controller.switch_frame(LeagueLeaderboard))

        pro_play = tk.Button(side_nav, text="Pro Matches",
                             width=20, height=2, highlightthickness=0, bd=0,
                             font=self.side_nav_font, bg="#2b2b2b", fg="white",
                             command=lambda: controller.switch_frame(ProPlay))

        personal_stats = tk.Button(side_nav, text="League Personal Stats",
                                   width=20, height=2, highlightthickness=0, bd=0,
                                   font=self.side_nav_font, bg="#2b2b2b", fg="white",
                                   command=lambda: controller.switch_frame(PersonalStats))

        guides = tk.Button(side_nav, text="-> Guides",
                           width=20, height=2, highlightthickness=0, bd=0,
                           font=self.side_nav_font, bg="#2b2b2b", fg="white")

        valorant_lb = tk.Button(side_nav, text="Valorant Leaderboard",
                                width=20, height=2, highlightthickness=0, bd=0,
                                font=self.side_nav_font, bg="#2b2b2b", fg="white",
                                command=lambda: controller.switch_frame(ValorantLeaderboard))

        dir_widgets = [home, league_lb, pro_play, personal_stats, guides, valorant_lb]
        for idx in range(6):
            dir_widgets[idx].grid(row=idx, column=0)

        main_content_frame = tk.Frame(frame, bg="#2b2b2b", width=500, height=400)
        main_content_frame.grid(row=0, column=1)
        # Separate Valorant and League of Legends Guides by page/frame
        background_label = tk.Label(main_content_frame, image=self.guides_bg, bg="#2b2b2b")

        league_guides = tk.Button(main_content_frame, text="League Guides",
                                  height=2, highlightthickness=0, bd=0,
                                  font=self.side_nav_font, bg="#2b2b2b", fg="white",
                                  command=lambda: controller.switch_frame(LeagueGuides))
        valorant_guides = tk.Button(main_content_frame, text="Valorant Guides",
                                    height=2, highlightthickness=0, bd=0,
                                    font=self.side_nav_font, bg="#2b2b2b", fg="white",
                                    command=lambda: controller.switch_frame(ValorantGuides))
        dir_widgets.extend([league_guides, valorant_guides])

        lol_logo = tk.Label(main_content_frame, image=self.league_logo, bg="#2b2b2b")
        val_logo = tk.Label(main_content_frame, image=self.valorant_logo, bg="#2b2b2b")

        background_label.place(x=100, y=25)
        lol_logo.grid(row=0, column=0, padx=325)
        league_guides.grid(row=1, column=0)
        val_logo.grid(row=2, column=0)
        valorant_guides.grid(row=3, column=0)

        def hovering(e):
            e.widget["background"] = "gray"

        def not_hovering(e):
            e.widget["background"] = "#2b2b2b"

        dir_widgets.remove(guides)
        for widget in dir_widgets:
            widget.bind("<Enter>", hovering)
            widget.bind("<Leave>", not_hovering)

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

        self.create_guide_nav_buttons(controller)

    def create_guide_nav_buttons(self, controller):
        guide_nav_bar = tk.Frame(self, bg="#2b2b2b")
        guide_nav_bar.grid(row=2, column=0, sticky="news")

        guides_home = tk.Button(guide_nav_bar, text="To Guides Homepage",
                                width=30, highlightthickness=0, bd=0,
                                font=self.guide_nav_bar_font, bg="#2b2b2b", fg="white",
                                command=lambda: controller.switch_frame(Guides))
        league_guides = tk.Button(guide_nav_bar, text="-> League Guides",
                                  width=30, highlightthickness=0, bd=0,
                                  font=self.guide_nav_bar_font, bg="#2b2b2b", fg="white")
        valorant_guides = tk.Button(guide_nav_bar, text="To Valorant Guides",
                                    width=30, highlightthickness=0, bd=0,
                                    font=self.guide_nav_bar_font, bg="#2b2b2b", fg="white",
                                    command=lambda: controller.switch_frame(ValorantGuides))

        guide_nav_widgets = [guides_home, league_guides, valorant_guides]
        for idx in range(len(guide_nav_widgets)):
            guide_nav_widgets[idx].grid(row=0, column=idx)
        guide_nav_bar.grid_columnconfigure((0, 1, 2), weight=1, uniform="column")

        def hovering(e):
            e.widget["background"] = "gray"

        def not_hovering(e):
            e.widget["background"] = "#2b2b2b"

        for button in guide_nav_widgets:
            button.bind("<Enter>", hovering)
            button.bind("<Leave>", not_hovering)


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

        self.create_guide_nav_buttons(controller)

    def create_guide_nav_buttons(self, controller):
        guide_nav_bar = tk.Frame(self, bg="#2b2b2b")
        guide_nav_bar.grid(row=2, column=0, sticky="news")

        guides_home = tk.Button(guide_nav_bar, text="To Guides Homepage",
                                width=30, highlightthickness=0, bd=0,
                                font=self.guide_nav_bar_font, bg="#2b2b2b", fg="white",
                                command=lambda: controller.switch_frame(Guides))
        league_guides = tk.Button(guide_nav_bar, text="To League Guides",
                                  width=30, highlightthickness=0, bd=0,
                                  font=self.guide_nav_bar_font, bg="#2b2b2b", fg="white",
                                  command=lambda: controller.switch_frame(LeagueGuides))
        valorant_guides = tk.Button(guide_nav_bar, text="-> Valorant Guides",
                                    width=30, highlightthickness=0, bd=0,
                                    font=self.guide_nav_bar_font, bg="#2b2b2b", fg="white")

        guide_nav_widgets = [guides_home, league_guides, valorant_guides]
        for idx in range(len(guide_nav_widgets)):
            guide_nav_widgets[idx].grid(row=0, column=idx)
        guide_nav_bar.grid_columnconfigure((0, 1, 2), weight=1, uniform="column")

        def hovering(e):
            e.widget["background"] = "gray"

        def not_hovering(e):
            e.widget["background"] = "#2b2b2b"

        for button in guide_nav_widgets:
            button.bind("<Enter>", hovering)
            button.bind("<Leave>", not_hovering)


class ValorantLeaderboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2b2b2b")
        self.side_nav_font = font.Font(family="System", size=18)
        self.controller = controller

        page_title = tk.Label(self, text="RADIANT LEADERBOARD", height=2,
                              font=font.Font(family="System", size=32), bg="#2b2b2b", fg="white")
        page_title.grid(row=0, column=0, sticky="news", pady=10)
        break_line = tk.Label(self, text="", bg="white", height=0)
        break_line.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)

        page_content = tk.Frame(self, bg="#2b2b2b")
        page_content.grid(row=2, column=0, sticky="w")
        self.grid_rowconfigure(2, weight=1)

        self.create_side_nav(page_content, controller)

    def create_side_nav(self, frame, controller):
        side_nav = tk.Frame(frame, bg="#2b2b2b")
        side_nav.grid(row=0, column=0, sticky="w")

        home = tk.Button(side_nav, text="Home",
                         width=20, height=2, highlightthickness=0, bd=0,
                         font=self.side_nav_font, bg="#2b2b2b", fg="white",
                         command=lambda: controller.switch_frame(Homepage))

        league_lb = tk.Button(side_nav, text="League Leaderboard",
                              width=20, height=2, highlightthickness=0, bd=0,
                              font=self.side_nav_font, bg="#2b2b2b", fg="white",
                              command=lambda: controller.switch_frame(LeagueLeaderboard))

        pro_play = tk.Button(side_nav, text="Pro Matches",
                             width=20, height=2, highlightthickness=0, bd=0,
                             font=self.side_nav_font, bg="#2b2b2b", fg="white",
                             command=lambda: controller.switch_frame(ProPlay))

        personal_stats = tk.Button(side_nav, text="League Personal Stats",
                                   width=20, height=2, highlightthickness=0, bd=0,
                                   font=self.side_nav_font, bg="#2b2b2b", fg="white",
                                   command=lambda: controller.switch_frame(PersonalStats))

        guides = tk.Button(side_nav, text="Guides",
                           width=20, height=2, highlightthickness=0, bd=0,
                           font=self.side_nav_font, bg="#2b2b2b", fg="white",
                           command=lambda: controller.switch_frame(Guides))

        valorant_lb = tk.Button(side_nav, text="-> Valorant Leaderboard",
                                width=20, height=2, highlightthickness=0, bd=0,
                                font=self.side_nav_font, bg="#2b2b2b", fg="white")

        dir_widgets = [home, league_lb, pro_play, personal_stats, guides, valorant_lb]
        for idx in range(6):
            dir_widgets[idx].grid(row=idx, column=0)

        def hovering(e):
            e.widget["background"] = "gray"

        def not_hovering(e):
            e.widget["background"] = "#2b2b2b"

        dir_widgets.remove(valorant_lb)
        for widget in dir_widgets:
            widget.bind("<Enter>", hovering)
            widget.bind("<Leave>", not_hovering)

        created_by_label = tk.Label(self, text="Created by Darren Hoang, UCI, 2022",
                                    bg="#2b2b2b", fg="white", font=("Helvetica", 8))
        created_by_label.grid(row=7, column=0, sticky="sw")
        self.grid_rowconfigure(7, weight=1)


if __name__ == "__main__":
    app = RiotDirectoryApp()
    #for i in RiotAPI.get_personal_statistics("ChuuOnDeezNutz", "loona"):
        #print(i)
    #RiotAPI.get_radiant_valorant_leaderboard()
    app.mainloop()
