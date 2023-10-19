// Init Functions
function main() {
    horizontalDraggable()
}

//Functions
function horizontalDraggable() {
    const slider = document.querySelector('.horizontal-Draggable');
    let isDown = false;
    let startX;
    let scrollLeft;
    
    slider.addEventListener('mousedown', (e) => {
      isDown = true;
      slider.classList.add('active');
      startX = e.pageX - slider.offsetLeft;
      scrollLeft = slider.scrollLeft;
    });
    slider.addEventListener('mouseleave', () => {
      isDown = false;
      slider.classList.remove('active');
    });
    slider.addEventListener('mouseup', () => {
      isDown = false;
      slider.classList.remove('active');
    });
    slider.addEventListener('mousemove', (e) => {
      if(!isDown) return;
      e.preventDefault();
      const x = e.pageX - slider.offsetLeft;
      const walk = (x - startX) * 1;
      slider.scrollLeft = scrollLeft - walk;
      console.log(walk);
    });
}

function paginationSelect() {
  const removeTagsFrom = [...document.querySelectorAll(".pagination li")]

  removeTagsFrom.map((liElement) => {
    liElement.classList.remove("selected")
  })
}