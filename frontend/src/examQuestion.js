// Required Objects
Message = "";
Subject = "Biology"
Level = "GCSE";
Board = "AQA";

// Objects
Loading = document.getElementById("Loading"); // Allows the loading area to be toggled
QuestionAndAnswer = document.getElementById("QuestioAndAnswer"); // Allows the Question area to be toggled
AnswerArea =  document.getElementById("AnswerContainer"); // Allows the Answer area to be toggled

// Temporary Objectss
var QuestionLevelArray = ["GCSE", "A-Level"];
var QuestionSubjectArray = ["Biology", "Physics", "Chemistry", "Computer Science", "Maths"];
var QuestionExamboardArray = ["AQA"];


// Sets the webpage to its default look
function Default()
{
    Loading.style.display = "none";
    QuestionAndAnswer.style.display = "none";
    AnswerArea.style.display = "none";
    ShowAnswer(true);
    JSONSelect();
}


// Read JSON Select Elements
function JSONSelect(){ // Function reads external JSON file and stores its values   
    fetch("../assets/JSON/SelectElements.json")
        .then(res => res.json())
        .then(data => {
            // Changes the options given on the Select elements
            AddSelectElements("QuestionLevel",data.QuestionLevel);
            AddSelectElements("QuestionSubject",data.QuestionSubject);
            AddSelectElements("QuestionExamboard",data.QuestionExamboard);
        });
    
}

// Function for each Select element
function AddSelectElements(ID,Array)// Function reads an array and adds a new option
{
    CurrentSelect = document.getElementById(ID); // Stores the current select to add
    while (CurrentSelect.options.length > 0) { // Removes previous options
        CurrentSelect.remove(0);
    }
    for(i=0; i < Array.length ;i++) // Reads through given array and adds the element at the given position
    {
        OptionElement = document.createElement("option");
        NewChoice = document.createTextNode(Array[i]);
        OptionElement.appendChild(NewChoice); // Adds the new choice to the Option Element
        CurrentSelect.appendChild(OptionElement); // Adds new option to the Select element
    }
}

// Function reads current option and stores it
function OptionStore(ID, RequiredObject){
    Choice = document.getElementById(ID).value;
    console.log(Choice);
    
    if(Choice.includes("A-level")){
        Level = "A-Level";
        document.getElementById("QuestionLevel").selectedIndex = 1;
    }
    RequiredObject = Choice;
}

//Function for the Generate Question Button
function GenerateQuestion() 
{
    // Creates spinning circle
    ShowAnswer(true);
    Loading.style.display = "block";
    QuestionAndAnswer.style.display = "block"; /////
    DataToInput = {
        "message": Message,
        "subject": Subject,
        "level": Level,
        "board": Board
    }
    JSONData = JSON.stringify(DataToInput);
}

AnswerChoice = false;
AnswerButton = document.getElementById("AnswerButton")
function ShowAnswer(returntoDefault){
    if(AnswerChoice || returntoDefault){
        AnswerButton.innerHTML = "&darr;";
        AnswerArea.style.display = "none";
        AnswerChoice = false;
    }
    else{
        AnswerButton.innerHTML = "&uarr;";
        AnswerArea.style.display = "block";
        AnswerChoice = true;
    }
}

Default(); // Sets the webpage to its default layout


/*
Use Formdata to add create and store the input data
*/
var myform = document.getElementById("exam-question-spec");
myform.addEventListener("submit", async event =>{
    event.preventDefault()
    const formData = new FormData(myform);
    const data = new URLSearchParams(formData)
    try{
    const res = await fetch("http://127.0.0.1:5000/", {
        method: "POST",
        body: data,
    })
    Loading.style.display = "none";
    QuestionAndAnswer.style.display = "block";
    newdata = res.json().then((result)=>{
        question_data = result.split("Markscheme:")
        question = question_data[0] 
        question
        answer = question_data[1]
        output_question = document.getElementById("ActualQuestion")
        question = question.replace("Question: ","");
        output_question.innerHTML = question
        output_answer = document.getElementById("ActualAnswer")
        output_answer.innerHTML = answer
    })
    //
    //
    
    if(!res.ok){
        console.log("problem")
    }
    }
    catch(error){
        console.log(error)
    }
});