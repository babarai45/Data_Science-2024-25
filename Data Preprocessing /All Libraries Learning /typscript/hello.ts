import { stdin, stdout } from "deno";

async function main() {
  const reader = new TextDecoder().decode(await stdin.read());
  const number = parseInt(reader.trim());

  if (isNaN(number)) {
    console.log("Please enter a valid number.");
    return;
  }

  for (let i = 1; i <= 10; i++) {
    console.log(`${number} x ${i} = ${number * i}`);
  }
}

main();