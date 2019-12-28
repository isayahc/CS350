function average (n,q1,q2,q3){
    result={};
  
          for (let i=0; i<n.length; i++) 
          {  
              result[n[i]] = (q1[i]+q2[i]+q3[i])/3;  
          }
  
          return result;
  
      }

      names = ["Ian", "Adrian", "Daniel", "Malcolm", "Roberson", "William", "Yousif", "Nicholas"]; 
      quiz1 = [100, 100, 100, 100, 100, 100, 100, 100];  
      quiz2 = [90, 90, 90, 90, 90, 90, 90, 100];  
      quiz3 = [90, 80, 70, 60, 50, 40, 30, 100];

      students = average(names, quiz1, quiz2, quiz3);
  
      console.log(students);

/*
Error 1:
result[n[i]]=q1[i]+q2[i]+q3[i]/3; 
This is an error because of order of operations 

Error2:
for (var i=1; i<n.length; i++) 
The iterator should start at the 0th position

Error3:
Quiz2 and Quiz3 was missing data. The only way for 
Nicholas' average grade to be 100 is for all quizes to 
equate to 100.





*/
  