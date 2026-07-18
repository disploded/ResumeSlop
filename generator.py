import subprocess
import random
import data
import tempfile



def pick(arr):
    return random.choice(arr)


def run():
    pdf = tempfile.NamedTemporaryFile(
        suffix=".pdf",
        delete=False
    ).name


    values = {
        "name": pick(data.names),
        "email": pick(data.emails),
        "location": pick(data.locations),

        "institution": pick(data.institutions),
        "degree": pick(data.degrees),
        "gpa": pick(data.gpas),
        "award": pick(data.awards),
        "coursework": pick(data.coursework),

        "skills": ", ".join(random.sample(data.skills, 6)),
        "technologies": ", ".join(random.sample(data.technologies, 6)),
    }

    # Jobs
    for i in range(3):
        values[f"job{i}_company"] = pick(data.companies)
        values[f"job{i}_title"] = pick(data.job_titles)
        values[f"job{i}_location"] = pick(data.job_locations)

        values[f"job{i}_start"] = pick(data.dates)
        values[f"job{i}_end"] = pick(data.dates)

        bullets = random.sample(data.job_bullets, 3)

        for j in range(3):
            values[f"job{i}_bullet{j}"] = bullets[j]

    # Projects
    for i in range(2):

        values[f"project{i}_name"] = pick(data.projects)

        values[f"project{i}_start"] = pick(data.dates)
        values[f"project{i}_end"] = pick(data.dates)

        values[f"project{i}_description"] = pick(
            data.project_descriptions
        )

        bullets = random.sample(
            data.project_bullets,
            2
        )

        values[f"project{i}_bullet0"] = bullets[0]
        values[f"project{i}_bullet1"] = bullets[1]

    command = [
        "typst",
        "compile",
        "format.typ",
        pdf
    ]

    for key, value in values.items():
        command.extend([
            "--input",
            f"{key}={value}"
        ])

    subprocess.run(
        command,
        check=True
    )

    return pdf


if __name__ == "__main__":
    print(run())
