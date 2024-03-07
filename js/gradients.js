const tl = gsap.timeline({ defaults: { ease: "power1.out" } });

tl.to(".text", { y: "0%", duration: 0.5, stagger: 0.25 });
tl.to(".slider", { y: "-100%", duration: 1, delay: 0.25 });
tl.to(".intro", { y: "-100%", duration: 0.5 }, "-=1");

//for all elements called .special, if clicked, run the function
const specialElements = document.querySelectorAll(".special");
specialElements.forEach((element) => {
  element.addEventListener("click", () => {
    //if the element has the class .special, remove it
    if (element.classList.contains("special")) {
      const dialog = document.getElementById("dialogContent");

      // Set custom data property on the dialog element
      dialog.innerText =
        "The section will provide further elaboration on the selected topic. We will use it for any definitions or for explaining notation.";

      window.dialog.showModal();
      //if the element does not have the class .special, add it
    } else {
      element.classList.add("special");
    }
  });
});
