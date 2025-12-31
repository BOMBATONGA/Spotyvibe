# Spotyvibe

**A satirical, AI-powered music profiling system.** Created as a "first build" to master full-stack integration, OAuth2, and LLM orchestration. 

It gives a ruthless personal profile based on the spotify listening history.

---

### Technical Implementation
* **Frontend:** HTML5, CSS3 and vanilla JS
* **Backend:** Flask (Python) Microservice.
* **Security:** Implemented `flask-limiter` for rate-limiting and `.env` for credential isolation.
* **Authentication:** Full OAuth2 flow using the `Spotipy` library.
* **Intelligence:** Generative AI logic powered by `Google Gemini`.

### !! A Note on the Spotify Restriction
As of 2025, the Spotify Developer Policy restricts public quotas to registered entities. Therefore, this app is only usable in **"Demo Mode"**.

Please use the **"Demo Mode"** on the landing page to see the full UI/UX and logic without needing a whitelisted Spotify account.

### What I Learned
1. **API Interoperability:** Handling data exchange between two different third-party services.
2. **State Management:** Managing the transition from user consent to data retrieval to AI generation.
3. **Constraint-Driven Problem Solving:** Navigating the technical and legal limitations of third-party platforms (Spotify) by pivoting the product architecture for showcase purposes.
