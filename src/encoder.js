import sha256 from 'sha256';

export default function encode(text) {
  if (text !== '') {
    return sha256(text);
  }
  return text;
}
