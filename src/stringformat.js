/**
 * String format functions
 *
 */
const lpad = (prefix, num) => {
  let number = ""
  if (num < 10) {
    number = prefix + prefix + num
  } else if (num < 100) {
    number = prefix + num
  } else {
    number += num
  }
  return number
}

export {lpad}
