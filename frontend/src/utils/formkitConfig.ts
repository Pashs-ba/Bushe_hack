export const formkitConfig = {
  global: {
    outer: '$reset form-group',
    input: 'form-control',
    label: 'form-label',
    messages: 'list-unstyled small mb-0',
    message: 'is-invalid',
    help: 'form-text'
  },
  checkbox: {
    label: 'form-check-label',
    wrapper: 'checkbox-wrapper',
    inner: 'form-check',
    input: '$reset form-check-input',
    legend: '$reset form-check-label'
  },
  select: {
    input: '$reset form-select'
  },
  radio: {
    label: 'form-check-label',
    wrapper: 'radio-wrapper',
    inner: 'form-check',
    input: '$reset form-check-input',
    legend: '$reset form-check-label'
  },
  submit: {
    outer: '$reset mt-3',
    input: '$reset btn btn-outline-light px-4'
  }
}
