import React from 'react';
import Summary from './Summary';

function Results({ answers, evaluations, onRestart }) {
  return (
    <div className="container fade-in">
      <div className="geometric-bg"></div>

      <div style={{ marginBottom: '40px', textAlign: 'center' }}>
        <h1>Interview Complete</h1>
        <p className="subtitle">
          Review your performance and detailed AI feedback below
        </p>
      </div>

      <Summary answers={answers} evaluations={evaluations} />

      <h2 style={{ marginBottom: '30px', marginTop: '60px' }}>Detailed Feedback</h2>

      {answers.map((item, index) => {
        const evaluation = evaluations[index];
        const score = evaluation?.score || 0;
        const scoreClass = score >= 7 ? 'high' : score >= 5 ? 'medium' : 'low';

        return (
          <div key={index} className="evaluation-card fade-in" style={{ animationDelay: `${index * 0.1}s` }}>
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '25px', marginBottom: '25px' }}>
              <div className={`score-badge ${scoreClass}`}>
                {score}/10
              </div>
              <div style={{ flex: 1 }}>
                <h3 style={{ marginBottom: '10px' }}>Question {index + 1}</h3>
                <div className="question-text" style={{ 
                  fontSize: '1.1rem', 
                  color: 'var(--bauhaus-blue)',
                  marginBottom: '15px'
                }}>
                  {item.question}
                </div>
              </div>
            </div>

            <div className="feedback-section">
              <div style={{ 
                background: 'var(--bauhaus-white)', 
                padding: '20px',
                border: '2px solid var(--bauhaus-black)',
                marginBottom: '20px'
              }}>
                <strong style={{ display: 'block', marginBottom: '10px', fontSize: '0.9rem', textTransform: 'uppercase' }}>
                  Your Answer:
                </strong>
                <p style={{ lineHeight: '1.8', color: 'var(--bauhaus-gray)' }}>
                  {item.answer}
                </p>
              </div>

              {evaluation && (
                <>
                  {evaluation.strengths && evaluation.strengths.length > 0 && (
                    <div style={{ marginBottom: '20px' }}>
                      <div className="feedback-title strengths">
                        Strengths
                      </div>
                      <ul className="feedback-list">
                        {evaluation.strengths.map((strength, i) => (
                          <li key={i}>{strength}</li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {evaluation.weaknesses && evaluation.weaknesses.length > 0 && (
                    <div style={{ marginBottom: '20px' }}>
                      <div className="feedback-title weaknesses">
                        Areas for Improvement
                      </div>
                      <ul className="feedback-list">
                        {evaluation.weaknesses.map((weakness, i) => (
                          <li key={i}>{weakness}</li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {evaluation.improved_answer && (
                    <div>
                      <div className="feedback-title improved">
                        Improved Answer Example
                      </div>
                      <div className="improved-answer-box">
                        {evaluation.improved_answer}
                      </div>
                    </div>
                  )}
                </>
              )}
            </div>
          </div>
        );
      })}

      <div className="button-group" style={{ marginTop: '50px' }}>
        <button onClick={onRestart} className="button-blue">
          Start New Interview
        </button>
      </div>

      <div style={{
        marginTop: '60px',
        padding: '30px',
        background: 'var(--bauhaus-white)',
        border: '3px solid var(--bauhaus-black)',
        textAlign: 'center'
      }}>
        <h3 style={{ marginBottom: '15px' }}>Keep Practicing</h3>
        <p style={{ color: 'var(--bauhaus-gray)', marginBottom: '20px' }}>
          Consistent practice is key to interview success. Try different roles and difficulty levels
          to expand your skills.
        </p>
        <button onClick={onRestart} className="button-yellow">
          Practice Another Role
        </button>
      </div>
    </div>
  );
}

export default Results;
