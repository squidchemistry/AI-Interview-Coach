const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const interviewAPI = {
  async generateQuestions(role, experience) {
    const response = await fetch(`${API_BASE_URL}/v1/interview/generate-questions`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ role, experience })
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.error?.message || `Failed to generate questions: ${response.statusText}`);
    }

    return response.json();
  },

  async evaluateAnswer(question, answer) {
    const response = await fetch(`${API_BASE_URL}/v1/interview/evaluate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question, answer })
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.error?.message || `Failed to evaluate answer: ${response.statusText}`);
    }

    return response.json();
  },

  async ping() {
    const response = await fetch(`${API_BASE_URL}/ping`);
    return response.json();
  }
};
