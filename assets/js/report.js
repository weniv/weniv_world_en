const btnDownload = document.querySelector('.btn-report');

const fetchQuestionInfo = async () => {
    const response = await fetch(
        `${window.location.origin}/assets/data/story/story.json`,
    );
    const jsonData = await response.json();
    return jsonData;
};

const getCode = (id) => {
    const codes = JSON.parse(localStorage.getItem(`${id}_code`));
    let codeText = '';
    // code를 순회하면서 요소를 추가
    codes.forEach((code) => {
        const trimedCode = code.trim();
        if (trimedCode) {
            codeText += '```py\n' + trimedCode + '\n```\n';
        }
    });
    return codeText ? codeText : '```py\n\n```';
};

const getTable = (chartData) => {
    return new Promise((resolve) => {
        let result = '|Subject|Progress|Score|\n|:---:|:---|:---:|\n';
        for (const key of Object.keys(chartData)) {
            result += `|${key} |${
                '◼︎'.repeat(chartData[key] / 10) +
                '◻︎'.repeat(10 - chartData[key] / 10)
            }|${chartData[key]}|\n`;
        }
        // return resolve(result);
        return resolve('');
    });
};

const downloadFile = async ({ data, fileName, fileType }) => {
    const blob = new Blob([data], { type: fileType });
    const link = document.createElement('a');

    link.download = fileName;
    link.href = await URL.createObjectURL(blob);

    const clickEvt = new MouseEvent('click', {
        view: window,
        bubbles: true,
        cancelable: true,
    });
    link.dispatchEvent(clickEvt);
    link.remove();
};

btnDownload.addEventListener('click', (e) => {
    const score = {
        'Variable and Data Types': 0,
        Operation: 0,
        'Iterative and Conditional Statement': 0,
        Function: 0,
        Class: 0,
    };

    let reportData = '';
    const questionData = fetchQuestionInfo();
    questionData.then((data) => {
        data.forEach((story) => {
            id = story['id'];
            if (localStorage.getItem(`${id}_code`)) {
                const result =
                    localStorage.getItem(`${id}_check`) === 'answer'
                        ? 'P'
                        : 'F';
                // evaluation 항목에 따라 점수를 부여한다.
                if (result == 'Y' && story['evaluation']) {
                    for (const key of story['evaluation']) {
                        score[key] += 10;
                    }
                }
                // const storyData = `## 문제 ${id}번\n\n* 평가 항목 : ${
                const storyData = `## EP ${id}\n\n* Submission Time : ${
                    localStorage.getItem(`${id}_time`) || '-'
                }\n* P/F : ${result}\n\n${getCode(id)}\n\n`;

                reportData += storyData;
            }
        });
        'score', score;
        // 표로 가져오기
        getTable(score).then((res) => {
            reportData = `# Study Report\n\n ${res}\n\n` + reportData;

            // TODO: 학번과 이름을 입력받아 파일명을 만들어준다.
            const userName =
                JSON.parse(localStorage.getItem('profile'))?.name || '[Name]';
            if (!!reportData) {
                const fileName = `Report`;
                const today = new Date();
                downloadFile({
                    data: reportData,
                    fileName: `${today
                        .toISOString()
                        .slice(2, 10)
                        .replace(/-/g, '')}_${fileName}_${userName}.md`,
                    fileType: 'text/json',
                });
            } else {
                window.alert('There is no data to download.');
            }
        });
    });
});
