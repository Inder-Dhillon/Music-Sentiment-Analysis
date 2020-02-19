function fun1() {
    var outputObj=document.getElementById("output");
    //outputObj.style = "text-align: left; font-size: 17px"
  
    var num = parseInt(prompt("Please enter a number: ", "") );
    
    var prime = true;
    var d = 2;
  
    while (prime == true && d <= num / 2) {
      if (num % d == 0) {
        prime = false;
      }
      d += 1;
    }
    if (prime) {
      outputObj.innerHTML="is prime";
    } else {
      outputObj.innerHTML="is not prime";
    }
    //outputObj.innerHTML += "<br><br>"+"program ended";
    //document.getElementsByTagName("button")[0].setAttribute("disabled","true");
  }
  
  function fun2() {
    var outputObj=document.getElementById("output");
    //outputObj.style = "text-align: left; font-size: 17px"
  
    var num;
    var sum1 = 0;
    var sum1 = 0;
  
    for (let i = 1; i <= 4; i++) {
      num = parseInt(prompt("Please enter a number: ", "") );
      sum1 += num;
    }
    for (let i = 1; i <= 4; i++) {
      num = parseInt(prompt("Please enter a number: ", "") );
      sum2 += num;
    }
    if (sum1 == sum2) {
      outputObj.innerHTML = "yes";
    } else {
      outputObj.innerHTML = "no";
    }
  
  }
  
  function fun3() {
    var outputObj=document.getElementById("output");
    //outputObj.style = "text-align: left; font-size: 17px"
  
    var p = 0;
    var n = 0;
    do{
      num = parseInt(prompt("Please enter a number: ", "") );
      if (num > 0 ) {
        p += 1;
      } else if (num < 0) {
        n += 1;
      }
    } while (num != 0 && p >= 2*n) {}
    outputObj.innerHTML = "p = " + p + ", q = " +q;
  }
  
  function fun4() {
    var outputObj=document.getElementById("output");
    //outputObj.style = "text-align: left; font-size: 17px"
  
    var cnt1 = 0;
    var cnt2 = 0;
    for (let i = 1; i <= 4; i++) {
      num = parseInt(prompt("Please enter a number: ", "") );
      if (num < 0) {
        cnt1 += 1;
      }
    }
  
    for (let i = 1; i <= 4; i++) {
      num = parseInt(prompt("Please enter a number: ", "") );
      if (num > 0) {
        cnt2 += 1;
      }
    }
    if (cnt1 == cnt2) {
    outputObj.innerHTML = "yes";    
    } else {
    outputObj.innerHTML = "no";
    }
  }
  
  function fun5() {
    var outputObj=document.getElementById("output");
    num = parseInt(prompt("Please enter a number: ", "") );
    
    for (let i = 2; i <= num; i++) {
      num = parseInt(prompt("Please enter a number: ", "") );
      if (prime(i) ) {
        outputObj.innerHTML += i;
      }
    }
  }
  function prime(num) {
    var flag = true;
    var d = 2;
  
    while (flag && d <= num / 2) {
      if (num % d == 0) {
        flag = false;
      }
      d += 1;
    }
    return flag;
  }
  
  