# Input a list of student scores 

i = input("Enter student scores: \n") 

student_scores = i.split() 

for n in range(0, len(student_scores)): 

  student_scores[n] = int(student_scores[n]) 

   

#Method 1 
 

# highest = student_scores[0]   

# # set initial highest to the first score in the list 

# for n in range(0, len(student_scores) - 1):   

#   # iterate up to len(student_scores) - 1 

#   if student_scores[n+1] > highest:  # compare with highest 

#     highest = student_scores[n+1]  # assign new highest 

  

#Method 2 

highest_score = 0 

for score in student_scores: 

  if score > highest_score: 

    highest_score = score 

     

print(f"The highest score in the class is: {highest_score} ") 

 
