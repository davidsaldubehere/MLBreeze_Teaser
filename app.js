const typingText = Typify("#typify-text", {
  text: [
    "machine learning mathematics",
    "modern architectures",
    "the latest AI developments",
  ],
  delay: 60,
  loop: true,
  cursor: true,
  stringDelay: 800,
});
document.addEventListener("DOMContentLoaded", function () {
  const expressions = [
    "\\(\\mathbf{X} = \\begin{bmatrix} x_{1,1} & x_{1,2} & \\cdots & x_{1,n} \\\\ x_{2,1} & x_{2,2} & \\cdots & x_{2,n} \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ x_{m,1} & x_{m,2} & \\cdots & x_{m,n} \\end{bmatrix}\\)",
    "\\(\\mathbf{y} = \\begin{bmatrix} y_1 \\\\ y_2 \\\\ \\vdots \\\\ y_m \\end{bmatrix}\\)",
    "\\(\\mathbf{w} = \\begin{bmatrix} w_1 \\\\ w_2 \\\\ \\vdots \\\\ w_n \\end{bmatrix}\\)",
    "\\(\\mathbf{X}^T\\)",
    "\\(\\mathbf{X}^T \\mathbf{X}\\)",
    "\\(\\nabla J(\\mathbf{w}) = \\frac{1}{m} \\mathbf{X}^T (\\mathbf{X}\\mathbf{w} - \\mathbf{y})\\)",
    "\\(\\mathbf{w}_{new} = \\mathbf{w}_{old} - \\alpha \\nabla J(\\mathbf{w}_{old})\\)",
    "\\(\\sigma(z) = \\frac{1}{1 + e^{-z}}\\)",
    "\\(\\frac{\\partial J(\\mathbf{w})}{\\partial w_i} = \\frac{1}{m} \\sum_{i=1}^{m} (\\sigma(\\mathbf{w}^T \\mathbf{x}_i) - y_i) x_i\\)",
    // Add more machine learning related expressions as needed
  ];

  setInterval(function () {
    const expression = document.createElement("div");
    expression.classList.add("math-expression");
    expression.style.left = Math.random() * window.innerWidth - 100 + "px";
    expression.style.top = Math.random() * window.innerHeight - 100 + "px";
    expression.style.transform = "rotate(" + (Math.random() * 90 - 45) + "deg)"; // Random rotation between -45 and 45 degrees

    expression.innerHTML =
      expressions[Math.floor(Math.random() * expressions.length)];
    document.getElementById("background").appendChild(expression);

    setTimeout(function () {
      expression.remove();
    }, 5000); // Adjust fade out duration
    MathJax.typeset();
  }, 1000); // Adjust time between expression appearances
});
