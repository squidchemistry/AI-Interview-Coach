import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './components/Home';
import InterviewSetup from './components/InterviewSetup';
import InterviewSession from './components/InterviewSession';
import Results from './components/Results';
import { interviewAPI } from './services/api';

function App() {
  const [stage, setStage] = useState('setup'); // setup, interview, results
  const [interviewData, setInterviewData] = useState({
    role: '',
    experience: '',
    questions: []
  });
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [evaluations, setEvaluations] = useState([]);

  const startInterview = (role, experience, questions) => {
    setInterviewData({ role, experience, questions });
    setStage('interview');
    setCurrentQuestionIndex(0);
    setAnswers([]);
    setEvaluations([]);
  };

  const submitAnswer = async (answer) => {
    const question = interviewData.questions[currentQuestionIndex];
    const newAnswers = [...answers, { question, answer }];
    setAnswers(newAnswers);

    // Get evaluation from backend
    try {
      const evaluation = await interviewAPI.evaluateAnswer(question, answer);
      setEvaluations([...evaluations, evaluation]);
    } catch (error) {
      console.error('Error evaluating answer:', error);
      setEvaluations([...evaluations, { 
        score: 0, 
        strengths: [], 
        weaknesses: ['Error evaluating answer. Please try again.'], 
        improved_answer: 'Evaluation failed due to a technical error.' 
      }]);
    }

    // Move to next question or results
    if (currentQuestionIndex < interviewData.questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      setStage('results');
    }
  };

  const restart = () => {
    setStage('setup');
    setInterviewData({ role: '', experience: '', questions: [] });
    setCurrentQuestionIndex(0);
    setAnswers([]);
    setEvaluations([]);
  };

  return (
    <Router>
      <div className="App">
        <Navbar />

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/interview" element={
            <>
              {stage === 'setup' && <InterviewSetup onStart={startInterview} />}
              {stage === 'interview' && (
                <InterviewSession
                  question={interviewData.questions[currentQuestionIndex]}
                  questionNumber={currentQuestionIndex + 1}
                  totalQuestions={interviewData.questions.length}
                  onSubmit={submitAnswer}
                />
              )}
              {stage === 'results' && (
                <Results
                  answers={answers}
                  evaluations={evaluations}
                  onRestart={restart}
                />
              )}
            </>
          } />
        </Routes>

        <Footer />
      </div>
    </Router>
  );
}

export default App;
