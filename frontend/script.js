// =====================================================
// ESSAYLENS AI - FINAL FRONTEND JAVASCRIPT
// =====================================================

console.log("EssayLens AI frontend loaded successfully.");

const API_URL = "http://127.0.0.1:5000/analyze";


// =====================================================
// INITIALIZE
// =====================================================

document.addEventListener("DOMContentLoaded", function () {

    const button =
        document.getElementById("analyzeButton");

    if (!button) {
        console.error("Analyze button not found.");
        return;
    }

    button.addEventListener("click", analyzeEssay);

    console.log(
        "Analyze button connected successfully."
    );
});


// =====================================================
// ANALYZE ESSAY
// =====================================================

async function analyzeEssay(event) {

    if (event) {
        event.preventDefault();
    }

    console.log("Analyze Essay button clicked.");

    const topic =
        document.getElementById("topic").value.trim();

    const essay =
        document.getElementById("essay").value.trim();

    const button =
        document.getElementById("analyzeButton");

    const loading =
        document.getElementById("loading");


    // -------------------------------------------------
    // VALIDATION
    // -------------------------------------------------

    if (!topic) {
        alert("Please enter the essay topic.");
        return;
    }

    if (!essay) {
        alert("Please enter your essay.");
        return;
    }


    // -------------------------------------------------
    // LOADING
    // -------------------------------------------------

    button.disabled = true;
    button.textContent = "Analyzing...";

    if (loading) {
        loading.classList.remove("hidden");
        loading.style.display = "block";
    }


    try {

        console.log(
            "Sending essay to Flask API..."
        );


        // -------------------------------------------------
        // API REQUEST
        // -------------------------------------------------

        const response =
            await fetch(
                API_URL,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        topic: topic,
                        essay: essay
                    })
                }
            );


        console.log(
            "API response status:",
            response.status
        );


        if (!response.ok) {

            throw new Error(
                "Server returned HTTP " +
                response.status
            );
        }


        // -------------------------------------------------
        // JSON RESPONSE
        // -------------------------------------------------

        const result =
            await response.json();

        console.log(
            "Essay analysis result:",
            result
        );


        // -------------------------------------------------
        // DISPLAY EVERYTHING
        // -------------------------------------------------

        displayResults(result);


    } catch (error) {

        console.error(
            "Analysis error:",
            error
        );

        alert(
            "Analysis failed.\n\n" +
            error.message
        );


    } finally {

        button.disabled = false;
        button.textContent =
            "Analyze Essay →";

        if (loading) {

            loading.classList.add(
                "hidden"
            );

            loading.style.display =
                "none";
        }
    }
}


// =====================================================
// DISPLAY RESULTS
// =====================================================

function displayResults(result) {

    console.log(
        "Displaying EssayLens AI results."
    );


    // -------------------------------------------------
    // SHOW RESULT SECTION
    // -------------------------------------------------

    const resultSection =
        document.getElementById(
            "resultSection"
        );

    if (resultSection) {

        resultSection.classList.remove(
            "hidden"
        );

        resultSection.style.display =
            "block";

        resultSection.style.visibility =
            "visible";

        resultSection.style.opacity =
            "1";
    }


    // -------------------------------------------------
    // SCORES
    // -------------------------------------------------

    const content =
        Number(result.content) || 0;

    const relevance =
        Number(result.relevance) || 0;

    const organization =
        Number(result.organization) || 0;

    const grammar =
        Number(result.grammar) || 0;

    const vocabulary =
        Number(result.vocabulary) || 0;

    const total =
        Number(result.total) || 0;


    // -------------------------------------------------
    // TOTAL SCORE
    // -------------------------------------------------

    setText(
        "totalScore",
        total.toFixed(2)
    );

    setText(
        "ringScore",
        total.toFixed(2)
    );


    // -------------------------------------------------
    // OVERALL MESSAGE
    // -------------------------------------------------

    if (
        result.feedback &&
        result.feedback.overall
    ) {

        setText(
            "overallMessage",
            result.feedback.overall
        );
    }


    // -------------------------------------------------
    // SCORE BREAKDOWN
    // -------------------------------------------------

    setText(
        "contentScore",
        content.toFixed(2) + " / 25"
    );

    setText(
        "relevanceScore",
        relevance.toFixed(2) + " / 20"
    );

    setText(
        "organizationScore",
        organization.toFixed(2) + " / 20"
    );

    setText(
        "grammarScore",
        grammar.toFixed(2) + " / 15"
    );

    setText(
        "vocabularyScore",
        vocabulary.toFixed(2) + " / 20"
    );


    // -------------------------------------------------
    // PROGRESS BARS
    // -------------------------------------------------

    setWidth(
        "contentBar",
        content / 25 * 100
    );

    setWidth(
        "relevanceBar",
        relevance / 20 * 100
    );

    setWidth(
        "organizationBar",
        organization / 20 * 100
    );

    setWidth(
        "grammarBar",
        grammar / 15 * 100
    );

    setWidth(
        "vocabularyBar",
        vocabulary / 20 * 100
    );


    // -------------------------------------------------
    // SCORE RING
    // -------------------------------------------------

    updateScoreRing(total);


    // -------------------------------------------------
    // STRENGTHS
    // -------------------------------------------------

    displayStrengths(result);


    // -------------------------------------------------
    // WEAKNESSES
    // -------------------------------------------------

    displayWeaknesses(result);


    // -------------------------------------------------
    // PERFORMANCE ANALYSIS
    // -------------------------------------------------

    displayAnalysis(result);


    // -------------------------------------------------
    // SUGGESTIONS
    // -------------------------------------------------

    displaySuggestions(result);


    // -------------------------------------------------
    // RADAR CHART
    // -------------------------------------------------

    drawRadarChart(result);


    // -------------------------------------------------
    // STATISTICS
    // -------------------------------------------------

    displayStatistics(result);


    // -------------------------------------------------
    // SCROLL
    // -------------------------------------------------

    setTimeout(function () {

        if (resultSection) {

            resultSection.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }

    }, 200);


    console.log(
        "All results displayed successfully."
    );
}


// =====================================================
// SET TEXT
// =====================================================

function setText(id, value) {

    const element =
        document.getElementById(id);

    if (element) {
        element.textContent = value;
    }
}


// =====================================================
// SET WIDTH
// =====================================================

function setWidth(id, value) {

    const element =
        document.getElementById(id);

    if (element) {

        element.style.width =
            Math.max(
                0,
                Math.min(100, value)
            ) + "%";
    }
}


// =====================================================
// SCORE RING
// =====================================================

function updateScoreRing(score) {

    const ring =
        document.getElementById(
            "scoreRing"
        );

    if (!ring) {
        return;
    }


    const radius =
        Number(
            ring.getAttribute("r")
        );


    if (!radius) {
        return;
    }


    const circumference =
        2 * Math.PI * radius;


    const percentage =
        Math.max(
            0,
            Math.min(100, score)
        ) / 100;


    ring.style.strokeDasharray =
        circumference;


    ring.style.strokeDashoffset =
        circumference *
        (1 - percentage);
}


// =====================================================
// STRENGTHS
// =====================================================

function displayStrengths(result) {

    const container =
        document.getElementById(
            "strengths"
        );

    if (!container) {
        return;
    }


    const scores = [

        {
            name: "Content",
            score: Number(result.content) || 0,
            max: 25
        },

        {
            name: "Relevance",
            score: Number(result.relevance) || 0,
            max: 20
        },

        {
            name: "Organization",
            score: Number(result.organization) || 0,
            max: 20
        },

        {
            name: "Grammar",
            score: Number(result.grammar) || 0,
            max: 15
        },

        {
            name: "Vocabulary",
            score: Number(result.vocabulary) || 0,
            max: 20
        }
    ];


    const strengths =
        scores.filter(
            item =>
                item.score / item.max >= 0.70
        );


    container.innerHTML = "";


    if (strengths.length === 0) {

        container.innerHTML =
            "<div>No major strengths detected.</div>";

        return;
    }


    strengths.forEach(
        function (item) {

            const div =
                document.createElement(
                    "div"
                );

            div.textContent =
                "✓ " +
                item.name +
                " is a strength (" +
                item.score.toFixed(2) +
                "/" +
                item.max +
                ").";

            container.appendChild(div);
        }
    );
}


// =====================================================
// WEAKNESSES
// =====================================================

function displayWeaknesses(result) {

    const container =
        document.getElementById(
            "weaknesses"
        );

    if (!container) {
        return;
    }


    const scores = [

        {
            name: "Content",
            score: Number(result.content) || 0,
            max: 25
        },

        {
            name: "Relevance",
            score: Number(result.relevance) || 0,
            max: 20
        },

        {
            name: "Organization",
            score: Number(result.organization) || 0,
            max: 20
        },

        {
            name: "Grammar",
            score: Number(result.grammar) || 0,
            max: 15
        },

        {
            name: "Vocabulary",
            score: Number(result.vocabulary) || 0,
            max: 20
        }
    ];


    const weaknesses =
        scores.filter(
            item =>
                item.score / item.max < 0.70
        );


    container.innerHTML = "";


    if (weaknesses.length === 0) {

        container.innerHTML =
            "<div>No major weaknesses detected.</div>";

        return;
    }


    weaknesses.forEach(
        function (item) {

            const div =
                document.createElement(
                    "div"
                );

            div.textContent =
                "⚠ " +
                item.name +
                " can be improved (" +
                item.score.toFixed(2) +
                "/" +
                item.max +
                ").";

            container.appendChild(div);
        }
    );
}


// =====================================================
// PERFORMANCE ANALYSIS
// =====================================================

function displayAnalysis(result) {

    const container =
        document.getElementById(
            "analysis"
        );

    if (!container) {
        return;
    }


    container.innerHTML = "";


    const scores = [

        {
            name: "Content",
            score: Number(result.content) || 0,
            max: 25
        },

        {
            name: "Relevance",
            score: Number(result.relevance) || 0,
            max: 20
        },

        {
            name: "Organization",
            score: Number(result.organization) || 0,
            max: 20
        },

        {
            name: "Grammar",
            score: Number(result.grammar) || 0,
            max: 15
        },

        {
            name: "Vocabulary",
            score: Number(result.vocabulary) || 0,
            max: 20
        }
    ];


    scores.forEach(
        function (item) {

            const percentage =
                item.score /
                item.max *
                100;


            let level;

            if (percentage >= 85) {
                level = "Excellent";
            }
            else if (percentage >= 70) {
                level = "Good";
            }
            else if (percentage >= 50) {
                level = "Needs Improvement";
            }
            else {
                level = "Needs Significant Improvement";
            }


            const div =
                document.createElement(
                    "div"
                );


            div.style.marginBottom =
                "10px";


            div.textContent =
                item.name +
                ": " +
                percentage.toFixed(1) +
                "% — " +
                level;


            container.appendChild(div);
        }
    );
}


// =====================================================
// SUGGESTIONS
// =====================================================

function displaySuggestions(result) {

    const container =
        document.getElementById(
            "suggestions"
        );

    if (!container) {
        return;
    }


    container.innerHTML = "";


    if (
        result.feedback &&
        result.feedback.suggestions &&
        result.feedback.suggestions.length > 0
    ) {

        result.feedback.suggestions.forEach(
            function (suggestion) {

                const div =
                    document.createElement(
                        "div"
                    );

                div.textContent =
                    "→ " + suggestion;

                container.appendChild(
                    div
                );
            }
        );

    } else {

        container.innerHTML =
            "<div>Continue practicing clear and well-structured writing.</div>";
    }
}


// =====================================================
// RADAR CHART
// =====================================================

function drawRadarChart(result) {

    const canvas =
        document.getElementById(
            "radarChart"
        );

    if (!canvas) {
        return;
    }


    const ctx =
        canvas.getContext("2d");


    if (!ctx) {
        return;
    }


    const width =
        canvas.width;

    const height =
        canvas.height;


    ctx.clearRect(
        0,
        0,
        width,
        height
    );


    const labels = [
        "Content",
        "Relevance",
        "Organization",
        "Grammar",
        "Vocabulary"
    ];


    const values = [

        (Number(result.content) || 0) / 25,

        (Number(result.relevance) || 0) / 20,

        (Number(result.organization) || 0) / 20,

        (Number(result.grammar) || 0) / 15,

        (Number(result.vocabulary) || 0) / 20
    ];


    const centerX =
        width / 2;

    const centerY =
        height / 2;

    const radius =
        Math.min(width, height) *
        0.30;


    function getPoint(index, distance) {

        const angle =
            -Math.PI / 2 +
            index *
            (2 * Math.PI / 5);


        return {

            x:
                centerX +
                Math.cos(angle) *
                distance,

            y:
                centerY +
                Math.sin(angle) *
                distance
        };
    }


    // -------------------------------------------------
    // GRID
    // -------------------------------------------------

    ctx.strokeStyle =
        "#cbd5e1";

    ctx.lineWidth = 1;


    for (
        let level = 1;
        level <= 5;
        level++
    ) {

        ctx.beginPath();


        for (
            let i = 0;
            i < 5;
            i++
        ) {

            const point =
                getPoint(
                    i,
                    radius *
                    level /
                    5
                );


            if (i === 0) {

                ctx.moveTo(
                    point.x,
                    point.y
                );

            } else {

                ctx.lineTo(
                    point.x,
                    point.y
                );
            }
        }


        ctx.closePath();

        ctx.stroke();
    }


    // -------------------------------------------------
    // AXES
    // -------------------------------------------------

    for (
        let i = 0;
        i < 5;
        i++
    ) {

        const point =
            getPoint(
                i,
                radius
            );


        ctx.beginPath();

        ctx.moveTo(
            centerX,
            centerY
        );

        ctx.lineTo(
            point.x,
            point.y
        );

        ctx.stroke();
    }


    // -------------------------------------------------
    // DATA SHAPE
    // -------------------------------------------------

    ctx.beginPath();


    values.forEach(
        function (value, index) {

            const point =
                getPoint(
                    index,
                    radius * value
                );


            if (index === 0) {

                ctx.moveTo(
                    point.x,
                    point.y
                );

            } else {

                ctx.lineTo(
                    point.x,
                    point.y
                );
            }
        }
    );


    ctx.closePath();


    ctx.fillStyle =
        "rgba(37, 99, 235, 0.18)";

    ctx.fill();


    ctx.strokeStyle =
        "#2563eb";

    ctx.lineWidth = 2;

    ctx.stroke();


    // -------------------------------------------------
    // LABELS
    // -------------------------------------------------

    ctx.fillStyle =
        "#334155";

    ctx.font =
        "14px Arial";

    ctx.textAlign =
        "center";

    ctx.textBaseline =
        "middle";


    labels.forEach(
        function (label, index) {

            const point =
                getPoint(
                    index,
                    radius + 35
                );


            ctx.fillText(
                label,
                point.x,
                point.y
            );
        }
    );
}


// =====================================================
// STATISTICS
// =====================================================

function displayStatistics(result) {

    const container =
        document.getElementById(
            "statistics"
        );

    if (!container) {
        return;
    }


    const features =
        result.features || {};

    const vocabulary =
        result.vocabulary_details || {};

    const organization =
        result.organization_details || {};


    container.innerHTML = "";


    const stats = [

        [
            "Words",
            features.word_count ??
            vocabulary.total_words ??
            0
        ],

        [
            "Sentences",
            features.sentence_count ??
            0
        ],

        [
            "Unique Words",
            features.unique_word_count ??
            vocabulary.unique_words ??
            0
        ],

        [
            "Paragraphs",
            features.paragraph_count ??
            organization.paragraph_count ??
            0
        ],

        [
            "Avg. Sentence Length",
            features.average_sentence_length ??
            0
        ],

        [
            "Lexical Diversity",
            features.lexical_diversity ??
            vocabulary.lexical_diversity ??
            0
        ]
    ];


    stats.forEach(
        function (item) {

            const div =
                document.createElement(
                    "div"
                );


            div.className =
                "stat-item";


            div.innerHTML =
                `
                <strong>${item[1]}</strong>
                <span>${item[0]}</span>
                `;


            container.appendChild(div);
        }
    );
}