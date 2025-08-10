"""
Physics Laws - Plain Statements & Basic Forms
(HTML formatted for PyQt QLabel)
"""

laws = [
    {
        "name": "Newton’s First Law of Motion (Law of Inertia)",
        "statement": "An object remains at rest or moves in a straight line with constant velocity unless acted on by a net external force.",
        "equation": "If F<sub>net</sub> = 0, then v = constant → a = 0"
    },
    {
        "name": "Newton’s Second Law of Motion",
        "statement": "The net force on an object equals the rate of change of its momentum.",
        "equation": "F<sub>net</sub> = dp/dt, and for constant mass: F = m·a"
    },
    {
        "name": "Newton’s Third Law of Motion",
        "statement": "For every action force, there is an equal and opposite reaction force.",
        "equation": "F<sub>AB</sub> = -F<sub>BA</sub>"
    },
    {
        "name": "Law of Universal Gravitation",
        "statement": "Two point masses attract with a force proportional to the product of their masses and inversely proportional to the square of the distance between them.",
        "equation": """
        <div style='text-align:center;'>
            <span style='border-bottom:2px solid;'>
                G · m<sub>1</sub> · m<sub>2</sub>
            </span><br>
            r<sup>2</sup>
        </div>
        """
    },
    {
        "name": "Law of Conservation of Energy",
        "statement": "The total energy of an isolated system remains constant.",
        "equation": "dE<sub>total</sub> / dt = 0"
    },
    {
        "name": "Law of Conservation of Momentum",
        "statement": "The total momentum of an isolated system remains constant.",
        "equation": "dP<sub>total</sub> / dt = 0"
    },
    {
        "name": "Ohm’s Law",
        "statement": "The current through a conductor is proportional to voltage and inversely proportional to resistance.",
        "equation": "V = I·R"
    },
    {
        "name": "Hooke’s Law",
        "statement": "The restoring force of a spring is proportional to its displacement.",
        "equation": "F = -k·x"
    },
    {
        "name": "Coulomb’s Law",
        "statement": "The electrostatic force between two point charges is proportional to their product and inversely proportional to the square of their separation.",
        "equation": """
        <div style='text-align:center;'>
            <span style='border-bottom:2px solid;'>
                k<sub>e</sub> · q<sub>1</sub> · q<sub>2</sub>
            </span><br>
            r<sup>2</sup>
        </div>
        """
    },
    {
        "name": "Faraday’s Law of Electromagnetic Induction",
        "statement": "A changing magnetic flux through a circuit induces an electromotive force (emf).",
        "equation": """
        <div style='text-align:center;'>
            ε = -
            <span style='border-bottom:2px solid;'>
                dΦ<sub>B</sub>
            </span><br>
            dt
        </div>
        """
    }
]
