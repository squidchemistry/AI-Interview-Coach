# How to Update Your Social Links

## Update LinkedIn and GitHub URLs

You need to replace the placeholder URLs with your actual profile links in two files:

### 1. Footer Component (`src/components/Footer.js`)

Find and replace these lines:

```javascript
// Line ~52 - LinkedIn URL
href="https://www.linkedin.com/in/your-profile"

// Line ~73 - GitHub URL  
href="https://github.com/your-username"
```

Replace with your actual URLs:
```javascript
href="https://www.linkedin.com/in/YOUR-ACTUAL-LINKEDIN-USERNAME"
href="https://github.com/YOUR-ACTUAL-GITHUB-USERNAME"
```

### 2. Navbar Component (`src/components/Navbar.js`)

Find and replace this line:

```javascript
// Line ~78 - GitHub URL in navbar
href="https://github.com/your-username"
```

Replace with:
```javascript
href="https://github.com/YOUR-ACTUAL-GITHUB-USERNAME"
```

Also update the mobile menu GitHub link:

```javascript
// Line ~138 - GitHub URL in mobile menu
href="https://github.com/your-username"
```

## Example:

If your GitHub username is `johndoe` and LinkedIn is `john-doe-dev`:

```javascript
// Footer.js
href="https://www.linkedin.com/in/john-doe-dev"
href="https://github.com/johndoe"

// Navbar.js
href="https://github.com/johndoe"
```

## Quick Find & Replace:

You can use your editor's find and replace feature:

1. Find: `https://www.linkedin.com/in/your-profile`
   Replace with: Your actual LinkedIn URL

2. Find: `https://github.com/your-username`
   Replace with: Your actual GitHub URL

That's it! Your social links will now point to your actual profiles.
