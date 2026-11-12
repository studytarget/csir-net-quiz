/* CSIR NET Quiz Portal - shared database settings (optional)
 *
 * While this stays `null`, the portal runs in "this device only" mode: accounts, scores and leaderboards live in
 * each browser's own storage, so candidates cannot see each other.
 *
 * To switch on shared accounts, attempt history and leaderboards for everyone, follow FIREBASE_SETUP.md, then replace
 * `null` below with the settings object Firebase shows you (Project settings > Your apps > Web app), for example:
 *
 * window.CSIR_FIREBASE_CONFIG = {
 *   apiKey: "AIza...",
 *   authDomain: "your-project.firebaseapp.com",
 *   projectId: "your-project",
 *   storageBucket: "your-project.firebasestorage.app",
 *   messagingSenderId: "1234567890",
 *   appId: "1:1234567890:web:abcdef123456"
 * };
 *
 * These values are not secrets: they identify the project, and the Firestore rules (firestore.rules) are what protect the data.
 */
window.CSIR_FIREBASE_CONFIG = null;
