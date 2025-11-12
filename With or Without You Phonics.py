
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>With or Without You : U2 : Phonics</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/react@17/umd/react.development.js" crossorigin></script>
  <script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js" crossorigin></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
</head>
<body class="bg-gray-100">
  <div id="root" class="flex justify-center items-center min-h-screen"></div>

  <script type="text/babel">
    const PhonicsQuiz = () => {
      const questions = [
        {
          word: 'Stone',
          options: [
            { text: '/stəʊn/', correct: false },
            { text: '/stoʊn/', correct: true },
            { text: '/stɒn/', correct: false },
            { text: '/stɔːn/', correct: false },
          ],
        },
        {
          word: 'Sleight of hand',
          options: [
            { text: '/slaɪt əv hænd/', correct: true },
            { text: '/sliːt əv hænd/', correct: false },
            { text: '/slət əv hænd/', correct: false },
            { text: '/sleɪkt əv hænd/', correct: false },
          ],
        },
        {
          word: 'Twist of fate',
          options: [
            { text: '/twɪs əv feɪt/', correct: false },
            { text: '/twɪst əv fæt/', correct: false },
            { text: '/twɪst əv feɪt/', correct: true },
            { text: '/twɪs əv fət/', correct: false },
          ],
        },
        {
          word: 'Bed of nails',
          options: [
            { text: '/bed əv neɪlz/', correct: false },
            { text: '/bed əv nælz/', correct: false },
            { text: '/bɛd əv neɪlz/', correct: true },
            { text: '/bæd əv neɪlz/', correct: false },
          ],
        },
        {
          word: 'Through',
          options: [
            { text: '/θruː/', correct: true },
            { text: '/θraʊ/', correct: false },
            { text: '/θrɒf/', correct: false },
            { text: '/θroʊ/', correct: false },
          ],
        },
        {
          word: 'Storm',
          options: [
            { text: '/stɔːm/', correct: false },
            { text: '/stɔːrm/', correct: true },
            { text: '/stɒrm/', correct: false },
            { text: '/stɜːrm/', correct: false },
          ],
        },
        {
          word: 'Shore',
          options: [
            { text: '/ʃoʊr/', correct: false },
            { text: '/ʃɔːr/', correct: true },
            { text: '/ʃɒr/', correct: false },
            { text: '/ʃʊr/', correct: false },
          ],
        },
        {
          word: 'Give yourself away',
          options: [
            { text: '/ɡɪv jɔːrˈself əˈweɪ/', correct: false },
            { text: '/ɡɪv jərˈself əˈweɪ/', correct: true },
            { text: '/ɡaɪv jɔːrˈself əˈweɪ/', correct: false },
            { text: '/ɡɪv jʊrˈself əˈweɪ/', correct: false },
          ],
        },
        {
          word: 'Tied',
          options: [
            { text: '/taɪd/', correct: true },
            { text: '/taɪt/', correct: false },
            { text: '/tiːd/', correct: false },
            { text: '/tɪd/', correct: false },
          ],
        },
        {
          word: 'Bruised',
          options: [
            { text: '/bru:st/', correct: false },
            { text: '/bruːzd/', correct: true },
            { text: '/brʊzd/', correct: false },
            { text: '/brʌɪzd/', correct: false },
          ],
        },
      ];

      const [currentQuestion, setCurrentQuestion] = React.useState(0);
      const [score, setScore] = React.useState(0);
      const [showScore, setShowScore] = React.useState(false);
      const [selectedAnswer, setSelectedAnswer] = React.useState(null);
      const [timeLimit, setTimeLimit] = React.useState(null);
      const [timeRemaining, setTimeRemaining] = React.useState(null);
      const [timerId, setTimerId] = React.useState(null);

      React.useEffect(() => {
        if (timeLimit !== null && timeRemaining > 0 && !showScore) {
          const id = setInterval(() => {
            setTimeRemaining(prev => {
              if (prev <= 1) {
                clearInterval(id);
                setShowScore(true);
                return 0;
              }
              return prev - 1;
            });
          }, 1000);
          setTimerId(id);
          
          return () => clearInterval(id);
        }
      }, [timeLimit, timeRemaining, showScore]);

      const handleAnswerClick = (option) => {
        setSelectedAnswer(option);

        if (option.correct) {
          setScore(score + 1);
          alert('Correct! 🎉');
        } else {
          alert('Incorrect. Try again. ❌');
        }

        setTimeout(() => {
          const nextQuestion = currentQuestion + 1;
          if (nextQuestion < questions.length) {
            setCurrentQuestion(nextQuestion);
            setSelectedAnswer(null);
          } else {
            setShowScore(true);
            clearInterval(timerId);
          }
        }, 1000);
      };

      const resetQuiz = () => {
        setCurrentQuestion(0);
        setScore(0);
        setShowScore(false);
        setSelectedAnswer(null);
        setTimeLimit(null);
        setTimeRemaining(null);
        clearInterval(timerId);
      };

      const handleTimeLimitChange = (limit) => {
        clearInterval(timerId);
        const newTimeLimit = limit ? limit * 60 : null;
        setTimeLimit(newTimeLimit);
        setTimeRemaining(newTimeLimit);
      };

      const formatTime = (seconds) => {
        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${mins}:${secs.toString().padStart(2, '0')}`;
      };

      return (
        <div className="w-full max-w-md mx-auto mt-10 bg-white shadow-lg rounded-lg p-6">
          <div className="text-center">
            <h1 className="text-2xl font-bold">With or Without You : U2 : Phonics</h1>
          </div>
          <div className="mt-4">
            {!showScore ? (
              <>
                <div className="flex justify-between mb-4">
                  <div>
                    Time Limit:
                    {[null, 3, 5, 7, 10].map((limit) => (
                      <button
                        key={limit}
                        className={`ml-2 px-3 py-1 rounded ${
                          timeLimit === (limit ? limit * 60 : null)
                            ? 'bg-blue-500 text-white'
                            : 'bg-gray-200'
                        }`}
                        onClick={() => handleTimeLimitChange(limit)}
                      >
                        {limit ? `${limit} min` : 'No Limit'}
                      </button>
                    ))}
                  </div>
                  {timeLimit !== null && (
                    <div className="text-red-500">
                      Time: {formatTime(timeRemaining)}
                    </div>
                  )}
                </div>
                <div className="mb-4">
                  <h2 className="text-xl font-bold">
                    Word: {questions[currentQuestion].word}
                  </h2>
                  <p className="text-sm text-gray-600">
                    Select the correct phonetic pronunciation
                  </p>
                </div>
                <div className="space-y-2">
                  {questions[currentQuestion].options.map((option, index) => (
                    <button
                      key={index}
                      className={`w-full px-4 py-2 rounded ${
                        selectedAnswer === option
                          ? option.correct
                            ? 'bg-green-500 text-white'
                            : 'bg-red-500 text-white'
                          : 'bg-gray-200'
                      }`}
                      onClick={() => handleAnswerClick(option)}
                      disabled={selectedAnswer !== null}
                    >
                      {option.text}
                    </button>
                  ))}
                </div>
                <div className="mt-4 text-center text-sm">
                  Question {currentQuestion + 1} of {questions.length}
                </div>
              </>
            ) : (
              <div className="text-center">
                <h2 className="text-2xl font-bold mb-4">Quiz Completed!</h2>
                <p className="text-xl mb-4">
                  Your Score: {score} / {questions.length}
                </p>
                <button
                  className="px-4 py-2 bg-blue-500 text-white rounded"
                  onClick={resetQuiz}
                >
                  Restart Quiz
                </button>
              </div>
            )}
            <div className="mt-4 text-xs text-gray-500 text-center">
              © 2025 Daniel Rojas :: TΣʃ :: ✉ CVO@tesh.pro
            </div>
          </div>
        </div>
      );
    };

    ReactDOM.render(<PhonicsQuiz />, document.getElementById('root'));
  </script>
</body>
</html>
