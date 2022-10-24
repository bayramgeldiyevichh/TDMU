//function to display questions
    //Question bank
    var questionBank= [
        {
            question : ' آ - harpy harpy türkmen dilinde haýsy harp',
            option : ['"P" harpy','"A" harpy','"G" harpy','"S" harpy'],
            answer : '"A" harpy'

        },
        {
            question : '<b> بابا </b> - "baba" - Türkmen dilinde näme diýmek',
            option : ['bölüm','kaka','erkek dogan','aýal dogan'],
            answer : 'kaka'
        },
        {
            question : '<b> پا </b> - "pa" - Türkmen dilinde name diýmek',
            option : ['bölüm','bilen','suw','aýak'],
            answer : 'aýak'
        },
        {
            question : '<b> اَست </b> - "äst" - sözi Türkmen dilinde näme many aňladýar ',
            option : ['howwa',' ýok','dyr,dir (goşulma)','dan,den (goşulma)'],
            answer : 'dyr,dir (goşulma)'
        },
        {
            question : '<b> تا  </b> - "ta" - sözi Türkmen dilinde näme many aňladýar',
            option : ['sany, çenli','taýak','odun','bolmak'],
            answer : 'sany, çenli'
        }
    ]

    var question= document.getElementById('question');
    var quizContainer= document.getElementById('quiz-container');
    var scorecard= document.getElementById('scorecard');
    var option0= document.getElementById('option0');
    var option1= document.getElementById('option1');
    var option2= document.getElementById('option2');
    var option3= document.getElementById('option3');
    var next= document.querySelector('.next');
    var points= document.getElementById('score');
    var span= document.querySelectorAll('span');
    var i=0;
    var score= 0;

    function displayQuestion(){
        for(var a=0;a<span.length;a++){
            span[a].style.background='none';
        } 
        question.innerHTML= 'Sorag.'+(i+1)+' ' +': '+questionBank[i].question;
        option0.innerHTML= questionBank[i].option[0];
        option1.innerHTML= questionBank[i].option[1];
        option2.innerHTML= questionBank[i].option[2];
        option3.innerHTML= questionBank[i].option[3];
        stat.innerHTML= "Sorag"+' '+questionBank.length + ' ' + 'den'+' '+(i+1);
    }

    //function to calculate score
    function calcScore(e){
        if(e.innerHTML===questionBank[i].answer && score<questionBank.length)
        {
            score= score+1;
            document.getElementById(e.id).style.background= 'limegreen';
        }
        else{
            document.getElementById(e.id).style.background= 'tomato';
        }
        setTimeout(nextQuestion,600);
    }

    //function to display next question
    function nextQuestion(){
        if(i<questionBank.length-1)
        {
            i=i+1;
            displayQuestion();
        }
        else{
            points.innerHTML= score+ '/'+ questionBank.length;
            quizContainer.style.display= 'none';
            scoreboard.style.display= 'block'
        }
    }

    //click events to next button
    next.addEventListener('click',nextQuestion);

    //back to quiz button event
    function backToQuiz(){
        location.reload();
    }

    //function to check Answers
    function checkAnswer(){
        var answerBank= document.getElementById('answerBank');
        var answers= document.getElementById('answers');
        answerBank.style.display= 'block';
        scoreboard.style.display= 'none';
        for(var a=0;a<questionBank.length;a++)
        {
            var list= document.createElement('li')
            list.innerHTML= questionBank[a].answer;
            answers.appendChild(list);
        }
    }

    displayQuestion();