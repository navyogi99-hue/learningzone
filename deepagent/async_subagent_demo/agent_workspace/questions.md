# Software Startup Freshers Assessment - Question Paper

This question paper contains 30 Multiple Choice Questions (MCQs) designed for freshers joining a software startup. The test is divided into three sections:
- **Section 1: Logical Reasoning** (Questions 1-10)
- **Section 2: Programming Fundamentals** (Questions 11-20)
- **Section 3: Professional Communication** (Questions 21-30)

Each question has exactly four choices.

---

## Section 1: Logical Reasoning

### Q1. Find the missing term in the alphabet series: FHJ, KMO, PRT, ?
A. UWY  
B. UWV  
C. VWY  
D. TUX  

### Q2. Pointing to a photograph, a person said, "She is the daughter of the woman who is the mother of the husband of my mother." How is the lady in the photograph related to this person?
A. Sister  
B. Aunt  
C. Mother  
D. Daughter  

### Q3. A man is facing West. He turns 45 degrees in the clockwise direction and then another 180 degrees in the same direction, and then 270 degrees in the anticlockwise direction. Which direction is he facing now?
A. South  
B. North-West  
C. South-West  
D. South-East  

### Q4. If INDIAN is coded as 91449114 in a certain language, how will the word THAI be coded in that same language?
A. 208110  
B. 20819  
C. 19819  
D. 20829  

### Q5. Consider the following statements and determine which of the conclusions logically follow:
**Statements:**
1. All C are J.
2. All J are B.
3. No B is R.

**Conclusions:**
I. All B are C.
II. Some J are C.

A. Only conclusion I follows  
B. Only conclusion II follows  
C. Both conclusion I and II follow  
D. Neither conclusion I nor II follows  

### Q6. Find the missing number in the following series: 5, 9, 18, 43, 92, 213, ?
A. 357  
B. 382  
C. 394  
D. 412  

### Q7. In a coding language used by a compiler development team, the word "STACK" is coded as "TVDGP". Under the same rules, how would the word "ARRAY" be coded?
A. BSUED  
B. BTUFC  
C. BTUED  
D. BTVEE  

### Q8. A programmable robot starts at the warehouse origin (0, 0) facing North. It executes the following sequence of movements:
1. Moves 15 meters forward.
2. Turns 90 degrees right and moves 12 meters.
3. Turns 90 degrees left and moves 10 meters.
4. Turns 180 degrees and moves 18 meters.
5. Turns 90 degrees left and moves 12 meters.

What is the shortest distance (in meters) between the robot's final position and its starting point?
A. 17 meters  
B. 25 meters  
C. 29 meters  
D. 35 meters  

### Q9. In a specialized family-tree simulation program, relationships are defined using symbolic operators:
- `A + B` means A is the father of B
- `A - B` means A is the wife of B
- `A * B` means A is the brother of B
- `A / B` means A is the daughter of B

Given the expression `P * Q / R - S + T`, how is P related to T?
A. Brother  
B. Uncle  
C. Cousin  
D. Father-in-law  

### Q10. Four developers (Alice, Bob, Charlie, and Diana) are assigned to four different startup projects (Frontend, Backend, Database, and DevOps), with exactly one developer per project. You are given the following clues:
1. Diana does not work on Frontend or Database.
2. Charlie is working on Backend.
3. Alice is not working on DevOps.
4. Alice is not working on Database.

Which project is Diana working on?
A. Frontend  
B. Database  
C. DevOps  
D. Backend  

---

## Section 2: Programming Fundamentals

### Q11. What is the average-case time complexity of searching for a key in a Python dictionary (hash table)?
A. O(1)  
B. O(log n)  
C. O(n)  
D. O(n log n)  

### Q12. Which of the following built-in data types in Python is mutable?
A. tuple  
B. list  
C. string  
D. int  

### Q13. In a standard Binary Search Tree (BST) containing unique values, what is the correct relationship between any parent node and its left and right subtrees?
A. All keys in the left subtree must be greater than the parent key, and all keys in the right subtree must be smaller.  
B. All keys in the left subtree must be smaller than the parent key, and all keys in the right subtree must be greater.  
C. The parent node must always have exactly two child nodes.  
D. The parent key is always the average of the left and right child keys.  

### Q14. Which of the following sorting algorithms has a worst-case time complexity of O(n^2) but can achieve a best-case time complexity of O(n) when optimized with a swap-check flag?
A. Merge Sort  
B. Quick Sort  
C. Bubble Sort  
D. Selection Sort  

### Q15. What will be the output of the following Python code snippet?
```python
my_list = [10, 20, 30, 40, 50]
print(my_list[-3:])
```
A. [10, 20, 30]  
B. [30, 40, 50]  
C. [40, 50]  
D. [20, 30, 40]  

### Q16. What is the output of the following Python function when called with an argument of 10?
```python
def calculate_sum(limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(calculate_sum(10))
```
A. 23  
B. 33  
C. 18  
D. 45  

### Q17. What will be the output of the following Python code?
```python
x = True
y = False
z = True
result = (x or y) and not (y or z)
print(result)
```
A. True  
B. False  
C. None  
D. SyntaxError  

### Q18. A software startup wants to design a background task processing system where tasks are executed in the exact order they are received. Which data structure is most appropriate for managing these tasks?
A. Stack  
B. Queue  
C. Binary Search Tree  
D. Hash Set  

### Q19. What is the output of the following Python code snippet?
```python
words = ["apple", "bat", "cherry"]
output = [len(w) for w in words if "a" in w]
print(output)
```
A. [5, 3]  
B. [5, 3, 6]  
C. [3, 6]  
D. [5]  

### Q20. What is the primary purpose of the following recursive Python function when given a positive integer n?
```python
def mystery_function(n):
    if n <= 1:
        return n
    return n * mystery_function(n - 1)
```
A. To find the sum of numbers from 1 to n.  
B. To compute the nth Fibonacci number.  
C. To calculate the factorial of n.  
D. To reverse a list of numbers.  

---

## Section 3: Professional Communication

### Q21. You are a fresher software engineer. You realize that you cannot meet the deadline for a critical feature deployment due tomorrow afternoon because of an unexpected third-party API outage. What is the most professional way to handle this with your manager?
A. Send an urgent Slack message tomorrow morning: "Hey, the API is down so I can't deploy the feature. It's not my fault."  
B. Email your manager immediately, explaining the root cause (the API outage), the current status, and proposing a revised timeline with alternative mitigation plans.  
C. Wait until tomorrow afternoon's standup to report the issue so you can explain yourself in person.  
D. Pull an all-nighter to write a custom workaround without telling anyone, hoping they won't notice the API change.  

### Q22. Identify the grammatically correct sentence from the choices below, paying attention to subject-verb agreement commonly used in business reporting:
A. Neither the lead architect nor the product managers is satisfied with the current database schema.  
B. Neither the lead architect nor the product managers are satisfied with the current database schema.  
C. Neither the lead architect nor the product managers was satisfied with the current database schema.  
D. Neither the lead architect or the product managers are satisfied with the current database schema.  

### Q23. You receive feedback on your first pull request from a senior engineer. The comments are direct and point out several design patterns that you implemented incorrectly, suggesting a complete refactor of two modules. What is the most constructive response?
A. Reply defensively to the comments, explaining that you followed the initial requirements and that their design suggestions are overly complex.  
B. Delete the branch, rebuild it quietly from scratch, and do not reply to any comments to avoid further confrontation.  
C. Reply to the PR comments thanking them for the guidance, and schedule a brief 10-minute sync to clarify the alternative design patterns and ensure alignment with best practices.  
D. Direct message the CTO or team lead to complain about the senior engineer's harsh tone and ask to be reassigned to a different reviewer.  

### Q24. Choose the word that best completes the sentence to convey a professional and proactive tone: 'To ensure our system can handle the upcoming Black Friday traffic surge, we must ________ the database queries to reduce response latency.'
A. curtail  
B. optimize  
C. exacerbate  
D. truncate  

### Q25. During a sprint, a marketing stakeholder direct messages you on Slack asking you to add a small feature to the customer onboarding page immediately because it will help an upcoming campaign. This feature was not included in the sprint planning. How should you respond?
A. Agree to build it immediately since it's 'small' and you want to be helpful to other teams.  
B. Politely explain that you are currently committed to sprint deliverables and suggest they channel the request through your Product Manager so it can be prioritized.  
C. Ignore the Slack message entirely to maintain focus on your current tasks.  
D. Respond, 'We cannot do this. You need to follow the proper process and not message developers directly.'  

### Q26. Which of the following is the most professional, action-oriented, and clear email subject line when asking a teammate to review a technical specification document?
A. HELP! Need feedback ASAP on this doc.  
B. Review Request: Technical Spec for User Auth Module [Due Friday, 5 PM]  
C. Technical Spec Document  
D. Hey, can you look at this when you have a minute?  

### Q27. Select the option that is most concise, grammatically correct, and uses active voice to express a professional status update.
A. The bug was identified by me, and the hotfix is being tested right now by our QA team.  
B. I identified the bug, and our QA team is testing the hotfix now.  
C. Having identified the bug, the hotfix is under test currently by our QA team.  
D. I identified the bug, the hotfix is being tested by our QA team.  

### Q28. When reaching out to a senior engineer on Slack for help with a technical blocker, which approach is most efficient and respects their time?
A. Sending 'Hi' or 'Hello' and waiting for them to reply before typing your question.  
B. Sending a single, detailed message stating what you are trying to do, what error you encountered (with code/logs), what steps you have already tried, and your availability.  
C. Mentioning them in a public channel with a message like: 'I am stuck. Please help.'  
D. Calling them directly on Zoom/Slack huddle without sending a message first, to explain the issue dynamically.  

### Q29. Read the following paragraph from a technical architecture document: 'While SQLite is sufficient for localized testing, our production environment must handle concurrent write requests from thousands of active clients. Consequently, we will deploy PostgreSQL for staging and production, ensuring we config connection pooling to prevent connection exhaustion under peak load.' Based on the text, which of the following statements is TRUE?
A. SQLite is recommended for both localized testing and staging environments.  
B. PostgreSQL is only necessary for the production environment, not staging.  
C. Connection pooling is implemented to handle localized testing limitations.  
D. SQLite is unsuitable for the production environment because of concurrent write requirements.  

### Q30. Your project lead gives you a task: 'Improve the performance of our database loader.' No other context or metrics are provided. What is the best initial step?
A. Immediately start rewriting the database indexing queries to make them faster.  
B. Spend three days researching academic papers on database optimization before beginning work.  
C. Ask the project lead clarifying questions to define success, such as: 'What is our current baseline latency, what is our target performance metric, and do we have a specific dataset size we are optimizing for?'  
D. Report the task as blocked and refuse to work on it until a detailed technical specification is written.  
