
//전체 교내 학과 선택
document.addEventListener("DOMContentLoaded", () => {
    buttons = document.querySelectorAll('#filter .button'); //버튼 지정 (배열)
    const defaultButton = document.getElementById('all'); // 기본값으로 지정할 버튼

    defaultButton.classList.replace("unchecked", "checked"); //초기에 표시
    if(defaultButton){console.log(1);} //django에서 값을 받아오면 완성

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            buttons.forEach(btn => btn.classList.replace("checked", "unchecked"));
            button.classList.replace("unchecked", "checked");
            if(button.value == '교내'){ //django에서 값을 받아오면 완성
                document.getElementById("depa").value = '교내';
                console.log(2);
            } else if(button.value == '학과'){
                document.getElementById("depa").value = '학과';
                console.log(3);
            } else if(button.value == '전체'){
                document.getElementById("depa").value = '전체';
                console.log(1);
            }
            document.getElementById("searchForm").submit();
        })
    });
})

// Sorting
function changeSelect_so(obj) {
    document.getElementById("so").value = obj.value;
    document.getElementById("searchForm").submit();
}

function changeSelect_end(obj) {
    document.getElementById("en").value = obj.value;
    document.getElementById("searchForm").submit();
}

function changeSelect_place(obj) {
    document.getElementById("pl").value = obj.value;
    document.getElementById("searchForm").submit();
}

function changeSelect_income(obj) {
    document.getElementById("inc").value = obj.value;
    document.getElementById("searchForm").submit();
}

// Search
document.getElementById('search').onkeydown = function(e) {
    if (e.key === 'Enter') {
        e.preventDefault();

        // ID가 "kw"인 요소의 값을 ID가 "search"인 요소의 값으로 설정
        document.getElementById("kw").value = document.getElementById("search").value;
        
        // ID가 "searchForm"인 폼을 제출
        document.getElementById("searchForm").submit();
    }
};
/*
//스크랩 기능
function scrap(star) {
    let star_img = star.querySelector("img");

    if (star.value == "none") { // value가 scraped로 바뀜
        star.value = "scraped";          
        star_img.src = "http://127.0.0.1:8000/static/images/icons/blink_star.svg";
    } else {
        star.value = "none";
        star_img.src = "http://127.0.0.1:8000/static/images/icons/star.svg";
    }   
}
*/