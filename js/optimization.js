const tl = gsap.timeline({ defaults: { ease: "power1.out" } });

tl.to(".text", { y: "0%", duration: 0.5, stagger: 0.25 });
tl.to(".slider", { y: "-100%", duration: 1, delay: 0.25 });
tl.to(".intro", { y: "-100%", duration: 0.5 }, "-=1");

function myFunction() {
  var x = document.getElementById("navbar");
  if (x.className === "nav") {
    x.className += " responsive";
  } else {
    x.className = "nav";
  }
}
