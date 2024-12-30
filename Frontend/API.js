async function fetchCourseContent(contentToFetch) {
    try {
      const response = await fetch('https://cos1.vercel.app/api/content');
  
      if (response.ok) {
        const data = await response.json();
        console.log('Course Content:', data[contentToFetch].content);
        localStorage.setItem("Content", JSON.stringify(data[contentToFetch].content));
        window.location.href = "Details.html";
      } else {
        console.error('Failed to fetch course content:', await response.json());
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }


 function downloadMaterials(filename) {
  fetch(`http://cos1.vercel.app/api/materials/?filename=${filename}`)
  .then((response) => {
    if (response.ok) {
      return response.blob();
    } else {
      throw new Error("File not found");
    }
  })
  .then((blob) => {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    a.remove();
  })
  .catch((error) => console.error("Error:", error));
}