// 28278 스택 2
const fs = require("fs");
// const input = fs.readFileSync(0, "utf-8").toString().trim().split("\n");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

const main = (N, ...orderText) => {
  const stack = Array(N).fill(0);
  let rear = 0;
  let answer = [];
  orderText.forEach((order) => {
    const [request, num] = order.split(" ").map(Number);
    switch (request) {
      case 1:
        stack[rear++] = num;
        break;
      case 2:
        answer.push(rear > 0 ? stack[--rear] : -1);
        break;
      case 3:
        answer.push(rear);
        break;
      case 4:
        answer.push(rear > 0 ? 0 : 1);

        break;

      default:
        answer.push(rear > 0 ? stack[rear - 1] : -1);

        break;
    }
  });
  console.log(answer.join("\n"));
};

main(...input);
