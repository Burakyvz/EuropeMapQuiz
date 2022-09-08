import turtle
import pandas

screen = turtle.Screen()
screen.title("Europe Country Game")

image = "euMap1.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coordinate(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinate)
# screen.mainloop()

data = pandas.read_csv("countries.csv")
all_countries = data.country.to_list()
guessed_countries = []

while len(guessed_countries) < 50:
    answer_country = screen.textinput(title=f"{len(guessed_countries)}/{len(all_countries)}",
                                      prompt="What's another country's name?").title()

    if answer_country == "Exit":
        missing_countries = [country for country in all_countries if country not in guessed_countries]
        new_data = pandas.DataFrame(missing_countries)
        new_data.to_csv("countries_to_learn.csv")
        break

    if answer_country in all_countries:
        guessed_countries.append(answer_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer_country]
        t.goto(int(country_data.x), int(country_data.y))
        t.write(answer_country, font=("Arial", 16, "normal"))