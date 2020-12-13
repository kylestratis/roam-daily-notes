import sys
import datetime


def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")


def custom_strftime(fmt, t):
    return t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day))


def calculate_retro_dates():
    today = datetime.date.today()
    retros = [
        custom_strftime("%B {S}, %Y", today - datetime.timedelta(weeks=i))
        for i in [1, 4, 12]
    ]
    retros.append(custom_strftime("%B {S}, %Y", today - datetime.timedelta(days=365)))
    retros.append(
        custom_strftime(
            "%B {S}, %Y", datetime.datetime.now().date().replace(month=1, day=1)
        )
    )
    return retros


def generate_template():
    retros = calculate_retro_dates()
    template = """
[[Daily Mantras]]
Meditate:: ---
Gym/Exercise::
Read for pleasure::
Read for learning::
Greek::
Bass::
## Retrospective
    One week ago: [[{one_week}]]
    Four weeks ago: [[{four_weeks}]]
    Twelve weeks ago: [[{twelve_weeks}]]
    365 days ago: [[{one_year}]]
## [[Tasks]]
    {{{{query: {{and: [[TODO]] {{not: {{or:[[Overdue Tasks]] [[Archive]]}}}} {{between: [[today]] [[today]]}}}}}}}}
## [[Overdue Tasks]]
    {{{{query: {{and: [[TODO]] {{not: {{or: [[query]] [[Archive]] [[Future]]}}}} {{between: [[yesterday]] [[{beginning_of_year}]]}}}}}}}}}}
## [[Completed Tasks]]
    {{{{query: {{and: [[DONE]] {{not: {{or: [[query]] [[Overdue Tasks]] [[Archive]]}}}} {{between: [[today]] [[today]]}}}}}}}}
## [[Tracking]]
    [[Sleep Score]]
        {{{{[[slider]]}}}}
    [[Morning Energy]]
        {{{{[[slider]]}}}}
    [[Cups of Coffee]]
        {{{{[[slider]]}}}}
    [[Afternoon Energy]]
        {{{{[[slider]]}}}}
## [[Journal]]
    [[Morning Pages]]
    """.format(
        one_week=retros[0],
        four_weeks=retros[1],
        twelve_weeks=retros[2],
        one_year=retros[3],
        beginning_of_year=retros[4],
    )
    return template


s = generate_template()
sys.stdout.write(s)
