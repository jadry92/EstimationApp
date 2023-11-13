function create_form_IO(id_row) {
  const form_IO_html = `
  <div class="row mt-2" id="${id_row}">
  <div class="offset-10 col-3">
    <button type="button" class="btn-close" aria-label="Close" id="${id_row}-close"></button>
  </div>
  <div class="col-3">
    <label for="IO-type" class="form-label">Type</label>
    <select class="form-select" id="IO-type" name="IO-type">
      <option value="DI">Digital Input</option>
      <option value="DO">Digital Output</option>
      <option value="AI">Analog Input</option>
      <option value="AO">Analog Output</option>
    </select>
  </div>
  <div class="col-6">
    <label for="IO-name" class="form-label">Name</label>
    <input type="text" class="form-control" id="IO-name" name="IO-name">
  </div>
  <div class="col-2">
    <label for="IO-amount" class="form-label">Amount</label>
    <input type="number" class="form-control" id="IO-amount" name="IO-amount" min="1">
  </div>
  <div class="form-check">
    <input class="form-check-input" type="checkbox" id="ExtraItem">
    <label class="form-check-label" for="ExtraItem">
      Extra Device Needed
    </label>
  </div>

  </div>
  `;

  return form_IO_html;
}
const button_add_IO = document.getElementById('addIO');
const IO_node = document.getElementById('IO-controller');
let number_IO = 0;

button_add_IO.addEventListener('click', (event) => {
  event.preventDefault();
  number_IO += 1;
  const id_row = `IO-${number_IO}`;
  const form_IO = create_form_IO(id_row);
  IO_node.insertAdjacentHTML('beforeend', form_IO);
  const button_remove_IO = document.getElementById(`${id_row}-close`);
  button_remove_IO.addEventListener('click', (event) => {
    event.preventDefault();
    const row = document.getElementById(id_row);
    row.remove();
  });
});

const button_add_fan = document.getElementById('addFan');
const fan_node = document.getElementById('fan-section');

let number_fan = 1;

button_add_fan.addEventListener('click', (event) => {
  event.preventDefault();
  number_fan += 1;
  const id_row = `fan-${number_fan}`;
  const form_fan = create_form_fan(id_row);
  fan_node.insertAdjacentHTML('beforeend', form_fan);
  const button_remove_fan = document.getElementById(`${id_row}-close`);
  button_remove_fan.addEventListener('click', (event) => {
    event.preventDefault();
    const row = document.getElementById(id_row);
    row.remove();
  });
});

function create_form_fan(id_row) {
  const form_fan_html = `
  <div class="input-group" id="${id_row}">
    <select class="form-select" name="fan-select">
      <option value="DI">Digital Input</option>
      <option value="DO">Digital Output</option>
      <option value="AI">Analog Input</option>
      <option value="AO">Analog Output</option>
    </select>
    <button class="btn btn-outline-danger btn-sm" type="button" id="${id_row}-close">
    <i class="bi bi-dash-square"></i> Remove
  </div>
  `;
  return form_fan_html;
}
