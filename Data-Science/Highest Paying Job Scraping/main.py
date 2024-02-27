from bs4 import BeautifulSoup
import requests
import time

url = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page"


def format_text(value):
    return value.text.split(":")[1]


def format_salary(value):
    return float(value.replace(",", "").replace("$", ""))


def format_high_meaning(value):
    if "%" in value:
        return float(value.replace("%", ""))
    return value


for page_num in range(1, 33):
    print("running page: ", page_num)
    response = requests.get(url=f"{url}/{page_num}")
    html_contents = response.text
    soup = BeautifulSoup(html_contents, "html.parser")
    # print(soup.title.string)
    table_titles = [title.text for title in soup.select(selector=".data-table__header")]
    # print(table_titles)
    ranks = [
        int(format_text(rank))
        for rank in soup.select(selector=".csr-col--rank")[1::]
    ]
    school_types = [
        format_text(school_type)
        for school_type in soup.select(selector=".csr-col--school-type")[1::]
    ]
    majors = [
        format_text(major)
        for major in soup.select(selector=".csr-col--school-name")[1::]
    ]
    salaries_ele = soup.select(selector=".csr-col--right")
    early_career_pay = [format_salary(format_text(salary)) for salary in salaries_ele[3::3]]
    mid_career_pay = [format_salary(format_text(salary)) for salary in salaries_ele[4::3]]
    high_meaning = [format_high_meaning(format_text(salary)) for salary in salaries_ele[5::3]]

    with open("highest_paying_jobs.csv", mode="a") as file:
        if page_num == 1:
            file.write(",".join(table_titles))
            file.write("\n")
        for i in range(len(ranks)):
            file.write(
                f"{ranks[i]},{majors[i]},{school_types[i]},{early_career_pay[i]},{mid_career_pay[i]},{high_meaning[i]}\n"
            )
    time.sleep(0.6)
