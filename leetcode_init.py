import sys
import requests


# Get first argument
argv = sys.argv[1]

# Get the problem name
slug = argv.split("/")[4]

headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "content-type": "application/json",
}

json_data = {
    "query": """
        query questionEditorData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            codeSnippets {
              lang
              langSlug
              code
            }
            exampleTestcaseList
          }
        }
    """,
    "variables": {
        "titleSlug": f"{slug}",
    },
    "operationName": "questionEditorData",
}

response = requests.post(
    "https://leetcode.com/graphql/", headers=headers, json=json_data
)

r = response.json()
code_snippet = r["data"]["question"]["codeSnippets"][3]["code"]


# Format number into 4 digit format
problem_number = r["data"]["question"]["questionFrontendId"]
problem_number = f"{int(problem_number):04}"

# Lowercase the name and change spaces to _
problem_name = slug.replace("-", "_")

filename = problem_number + "_" + problem_name + ".py"

exampleTestcaseList = r["data"]["question"]["exampleTestcaseList"]
for case in exampleTestcaseList:
    print(case)

test_cases = """
def case_one():
    pass


def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
"""

with open(filename, "w+") as f:
    f.write(code_snippet)
    f.write("pass\n")
    f.write(test_cases)
