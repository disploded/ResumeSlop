#import "@preview/basic-resume:0.2.9": *


#let name = sys.inputs.at("name")
#let email = sys.inputs.at("email")
#let location = sys.inputs.at("location")

#let institution = sys.inputs.at("institution")
#let degree = sys.inputs.at("degree")
#let gpa = sys.inputs.at("gpa")
#let award = sys.inputs.at("award")
#let coursework = sys.inputs.at("coursework")

#show: resume.with(
  author: name,
  location: location,
  accent-color: "#26428b",
  font: "New Computer Modern",
  paper: "us-letter",
  author-position: left,
  personal-info-position: left,
)


== Education

#edu(
  institution: institution,
  location: location,
  dates: dates-helper(
    start-date: "Aug 2023",
    end-date: "May 2027"
  ),
  degree: degree,
)

- Cumulative GPA: #gpa | #award
- Relevant Coursework: #coursework


== Work Experience


#work(
title: sys.inputs.at("job0_title"),
location: sys.inputs.at("job0_location"),
company: sys.inputs.at("job0_company"),
dates: dates-helper(
start-date: sys.inputs.at("job0_start"),
),
)

- #sys.inputs.at("job0_bullet0")
- #sys.inputs.at("job0_bullet1")
- #sys.inputs.at("job0_bullet2")



#work(
title: sys.inputs.at("job1_title"),
location: sys.inputs.at("job1_location"),
company: sys.inputs.at("job1_company"),
dates: dates-helper(
start-date: sys.inputs.at("job1_start"),
),
)

- #sys.inputs.at("job1_bullet0")
- #sys.inputs.at("job1_bullet1")
- #sys.inputs.at("job1_bullet2")



#work(
title: sys.inputs.at("job2_title"),
location: sys.inputs.at("job2_location"),
company: sys.inputs.at("job2_company"),
dates: dates-helper(
start-date: sys.inputs.at("job2_start"),
),
)

- #sys.inputs.at("job2_bullet0")
- #sys.inputs.at("job2_bullet1")
- #sys.inputs.at("job2_bullet2")



== Projects


#project(
name: sys.inputs.at("project0_name"),
dates: dates-helper(
start-date: sys.inputs.at("project0_start"),
),
)

- #sys.inputs.at("project0_description")
- #sys.inputs.at("project0_bullet0")
- #sys.inputs.at("project0_bullet1")



#project(
name: sys.inputs.at("project1_name"),
dates: dates-helper(
start-date: sys.inputs.at("project1_start"),
),
)

- #sys.inputs.at("project1_description")
- #sys.inputs.at("project1_bullet0")
- #sys.inputs.at("project1_bullet1")



== Skills

- *Skills*: #sys.inputs.at("skills")
- *Technologies*: #sys.inputs.at("technologies")
