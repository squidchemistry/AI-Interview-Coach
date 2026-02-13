# Application Routes

## Available URLs

After running `npm start`, your application will be available at `http://localhost:3000`

### All Pages:

1. **Home Page**
   - URL: `http://localhost:3000/`
   - Description: Landing page with overview of the AI Interview Coach features
   - Features: Hero section, feature cards, how it works section, call-to-action

2. **Interview Setup Page**
   - URL: `http://localhost:3000/interview`
   - Description: Configure your interview session (role and experience level)
   - Features: Form to input target role and experience level, generates AI questions

3. **Interview Session Page**
   - URL: `http://localhost:3000/interview` (automatically shown after setup)
   - Description: Active interview with questions and answer input
   - Features: Progress bar, question display, answer textarea, real-time evaluation

4. **Results Page**
   - URL: `http://localhost:3000/interview` (automatically shown after completing all questions)
   - Description: Detailed feedback and performance summary
   - Features: Performance summary, score breakdown, detailed feedback per question, improved answer suggestions

## Navigation Flow:

```
Home (/) 
  ↓
  [Click "Start Interview" or navigation link]
  ↓
Interview Setup (/interview)
  ↓
  [Fill form and click "Generate Interview Questions"]
  ↓
Interview Session (/interview)
  ↓
  [Answer all questions]
  ↓
Results (/interview)
  ↓
  [Click "Start New Interview" to restart]
  ↓
Back to Interview Setup
```

## How to Run:

1. Make sure your backend is running (usually on `http://localhost:8000`)
2. Start the frontend:
   ```
   npm start
   ```
3. Open your browser to `http://localhost:3000`

## Navigation Bar:

The app includes a sticky navigation bar with:
- Logo/Brand (links to home)
- Home link
- Start Interview link

You can navigate between pages at any time using these links.
