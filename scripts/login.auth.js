// @ts-check

import { googleAuth, login, studentDataIsSaved } from "./firebase.js";
import { disableFields, handleError } from "./utils.auth.js";

async function proceedWithLogin() {
  const dataIsSaved = await studentDataIsSaved();
  location.href = dataIsSaved ? "/" : "/auth/auth.html";
}

window.addEventListener("load", () => {
  // @ts-ignore
  lucide.createIcons();

  const googleBtn = document.querySelector("#google-auth");
  // @ts-ignore
  googleBtn.onclick = () => {
    disableFields();
    googleAuth().then(proceedWithLogin).catch(handleError);
  };

  const loginForm = document["login-form"];
  /** @param {Event} e */
  loginForm.onsubmit = (e) => {
    e.preventDefault();
    disableFields();
    login(loginForm.email.value, loginForm.password.value)
      .then(proceedWithLogin)
      .catch(handleError);
  };

  // reveal password
  // @ts-ignore
  document.querySelector("[data-lucide=eye]").onclick = (e) => {
    loginForm.password.type = "text";
    e.currentTarget.classList.add("!hidden");
    e.currentTarget.nextElementSibling.classList.remove("!hidden");
  };
  
  // hide password
  // @ts-ignore
  document.querySelector("[data-lucide=eye-off]").onclick = (e) => {
    loginForm.password.type = "password";
    e.currentTarget.classList.add("!hidden");
    e.currentTarget.previousElementSibling.classList.remove("!hidden");
  };
});
