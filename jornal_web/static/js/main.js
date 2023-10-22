// Init Functions
function main() {
  highlights();
  horizontalDraggable();
}

//Functions

// interface handleModalProps {
//   modalName: String
//   option: "open" | "close"
//   flex: boolean
// }

function handleModal(modalName, option, flex) { //handleModalProps
  const modal = document.querySelector(`.${modalName}`)
  modal.style.display = option == "open" ? flex ? 'flex' : 'block' : 'none'
}

function modalPostOptions_showMore() {
  handleModal('modalPostOptions_alltags', 'open', true)
  handleModal('modalPostOption_seeMore', 'close')
}

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

//Alternação do paginador
function paginationSelect(e) {
  const removeTagsFrom = [...document.querySelectorAll(".pagination li")]

  removeTagsFrom.map((liElement) => {
    liElement.classList.remove("selected")
  })
  e.classList.toggle('selected')
}


function highlights(){

  let slides = document.querySelectorAll('.slide_container');
  let btns = document.querySelectorAll('.nav_btn');
  let currentSlide = 0;
  let autoSlide = true;
  let autoSlideInterval;

  // Passagem manual
  var manualNav = (manual) => {
      slides.forEach((slide) => slide.classList.remove('active'));
      btns.forEach((btn) => btn.classList.remove('active'));

      slides[manual].classList.add('active');
      btns[manual].classList.add('active');

      currentSlide = manual;

      if (autoSlide) {
          // Reiniciar a passagem automática
          clearInterval(autoSlideInterval);
          autoSlideInterval = setInterval(repeat, 10000);
      }
  };

  btns.forEach((btn, i) => {
      btn.addEventListener("click", () => {
          manualNav(i);
      });
  });

  // Passagem automática
  const repeat = () => {
      slides[currentSlide].classList.remove('active');
      btns[currentSlide].classList.remove('active');

      currentSlide = (currentSlide === slides.length - 1) ? 0 : currentSlide + 1;

      slides[currentSlide].classList.add('active');
      btns[currentSlide].classList.add('active');
  };

  autoSlideInterval = setInterval(repeat, 10000);
}