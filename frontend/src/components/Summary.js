import React from 'react';

function Summary({ answers, evaluations }) {
  const totalScore = evaluations.reduce((sum, evaluation) => sum + (evaluation?.score || 0), 0);
  const averageScore = evaluations.length > 0 ? (totalScore / evaluations.length).toFixed(1) : 0;
  
  const getPerformanceLevel = (avg) => {
    if (avg >= 8) return { text: 'Excellent', color: '#4CAF50', emoji: '🌟' };
    if (avg >= 6) return { text: 'Good', color: 'var(--bauhaus-blue)', emoji: '👍' };
    if (avg >= 4) return { text: 'Fair', color: 'var(--bauhaus-yellow)', emoji: '📈' };
    return { text: 'Needs Work', color: 'var(--bauhaus-red)', emoji: '💪' };
  };

  const performance = getPerformanceLevel(averageScore);
  const strongAnswers = evaluations.filter(e => e?.score >= 7).length;
  const averageAnswers = evaluations.filter(e => e?.score >= 5 && e?.score < 7).length;
  const weakAnswers = evaluations.filter(e => e?.score < 5).length;

  return (
    <div className="summary-card">
      <h2>Performance Summary</h2>
      
      <div className="summary-stats">
        <div className="stat-item">
          <div className="stat-value" style={{ color: performance.color }}>
            {performance.emoji} {averageScore}
          </div>
          <div className="stat-label">Average Score</div>
          <div className="stat-sublabel" style={{ color: performance.color }}>
            {performance.text}
          </div>
        </div>

        <div className="stat-item">
          <div className="stat-value">{answers.length}</div>
          <div className="stat-label">Total Questions</div>
          <div className="stat-sublabel">Completed</div>
        </div>

        <div className="stat-item">
          <div className="stat-value" style={{ color: '#4CAF50' }}>
            {strongAnswers}
          </div>
          <div className="stat-label">Strong Answers</div>
          <div className="stat-sublabel">Score ≥ 7</div>
        </div>

        <div className="stat-item">
          <div className="stat-value" style={{ color: 'var(--bauhaus-yellow)' }}>
            {averageAnswers}
          </div>
          <div className="stat-label">Average Answers</div>
          <div className="stat-sublabel">Score 5-6</div>
        </div>
      </div>

      {weakAnswers > 0 && (
        <div style={{
          marginTop: '30px',
          padding: '20px',
          background: 'rgba(230, 57, 70, 0.1)',
          border: '3px solid var(--bauhaus-red)',
          color: 'white'
        }}>
          <strong style={{ display: 'block', marginBottom: '8px' }}>
            ⚠️ Focus Areas
          </strong>
          <p style={{ fontSize: '0.95rem', opacity: '0.95' }}>
            You have {weakAnswers} answer{weakAnswers > 1 ? 's' : ''} that need improvement. 
            Review the detailed feedback below to strengthen your responses.
          </p>
        </div>
      )}
    </div>
  );
}

export default Summary;
